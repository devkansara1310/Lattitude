from django.shortcuts import render
from rest_framework.response import Response
import csv
from django.http import HttpResponse
from rest_framework.views import APIView

class test(APIView):
    def post(self,request):
        FMT  = request.data.get('FMT')
        msg  = request.data.get('Message')
        if FMT:
            return Response({'code':1,'Message':msg})
        else:
            msg = msg.split(',')
            response = HttpResponse(
            content_type='text/csv',
                headers={'Content-Disposition': 'attachment; filename="somefilename.csv"'},
            )
            writer = csv.writer(response)
            writer.writerow(msg)
            return response
