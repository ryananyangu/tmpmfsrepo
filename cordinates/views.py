from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
import logging

import ast
import math

from .models import (
    Cordinate,
)



class CordinatesView(APIView):

    permission_classes = (IsAuthenticated,) 

    def post(self, request):
        logging.info(request.data + " for user "+ request.user.username)
        cordinates = "["+request.data+"]"

        # print(type(request.user))
        user = request.user

        # NOTE: eval is not safe to the server(can be used to exploit the server)
        try:
            casted_cordinates = ast.literal_eval(cordinates)
        except (ValueError , SyntaxError) as e:
            logging.error(str(e)+" for user "+user.username)
            return Response(data="Invalid Request", status=status.HTTP_400_BAD_REQUEST)

        try:
            response = shortest_distance(casted_cordinates,user)
        except TypeError as te:
            logging.error(str(te)+" for user "+user.username)
            return Response(data="Invalid Request", status=status.HTTP_400_BAD_REQUEST)

        return Response(data=response, status=status.HTTP_201_CREATED)

    def get(self, request):
        return Response(data=Cordinate.objects.filter(created_by=request.user).values(), status=status.HTTP_200_OK)


def shortest_distance(cordinates: list, user: User) -> dict:
    logging.info("Calculating shortest distance for request by "+user.username)
    result = {"cordinates": "", "distance": None}
    cordinates_set = list(set(cordinates))

    if len(cordinates_set) == 1:
        result["cordinates"] = str(cordinates_set[0])
        result["distance"] = 0
        return result

    for cordinate in cordinates_set:
        for compare_cord in cordinates_set:
            distance = distance_calc(cordinate, compare_cord)
            if distance is None:
                continue
            if result["distance"] is None or result["distance"] >= distance:
                cordinate_pair = str(cordinate)+","+str(compare_cord)
                build_result(result, cordinate_pair, distance)
    save_cordinate(result, cordinates, user)
    return result


def distance_calc(cordinate: tuple, compare_cord: tuple) -> float:
    logging.debug("distance calc points ["+str(cordinate)+","+str(compare_cord)+"]")
    current_x_cord, current_y_cord = cordinate
    compare_x_cord, compare_y_cord = compare_cord
    x_diff = current_x_cord-compare_x_cord
    y_diff = current_y_cord-compare_y_cord
    if x_diff == 0 and y_diff == 0:
        return None
    return math.sqrt((x_diff**2)+(y_diff**2))


def build_result(result: dict, cordinate_pair: str, distance: float) -> dict:
    logging.debug("Compile computation result "+cordinate_pair)
    if result["distance"] == distance:
        result["cordinates"] += "|" + cordinate_pair
        return result
    result["cordinates"] = cordinate_pair
    result["distance"] = distance
    return result


def save_cordinate(result: dict, cordinates: list, user: User):
    logging.debug("Saving cordinates for user  "+user.username)
    cord = Cordinate()
    cord.cordinates = str(cordinates)
    cord.distance = result["distance"]
    cord.output = result["cordinates"]
    cord.created_by = user
    cord.modified_by = user
    cord.save()
