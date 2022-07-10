from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
import json

from .serializers import *

from .models import *
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'příjímá data': '/import',
        'seznam záznamů': '/detail/<slug:name>',
        'detail záznamu':'/detail/<slug:name>/<int:id>',
    }
    
    return Response(api_urls)


@api_view(['GET'])
def records(request,name):
    name = name.lower()
    match name:
        case "attributename":
            record = AttributeName.objects.all()
            serializer = AttributeNameIdSerializer(record,many=True)
            return Response(serializer.data)
        case "attributevalue":
            record = AttributeValue.objects.all()
            serializer = AttributeValueIdSerializer(record,many=True)
            return Response(serializer.data)
        case "attribute":
            record = Attribute.objects.all()
            serializer = AttributeIdSerializer(record,many=True)
            return Response(serializer.data)
        case "product":
            record = Product.objects.all()
            serializer = ProductIdSerializer(record,many=True)
            return Response(serializer.data)
        case "productattributes":
            record = ProductAttributes.objects.all()
            serializer = ProductAttributesIdSerializer(record,many=True)
            return Response(serializer.data)
        case "productimage":
            record = ProductImage.objects.all()
            serializer = ProductImageIdSerializer(record,many=True)
            return Response(serializer.data)
        case "image":
            record = Image.objects.all()
            serializer = ImageIdSerializer(record,many=True)
            return Response(serializer.data)
        case "catalog":
            record = Catalog.objects.all()
            serializer = CatalogIdSerializer(record,many=True)
            return Response(serializer.data)
        case _:
            return Response()
            
            
@api_view(['GET'])
def detailOfRecord(request,name,id):
    name = name.lower()  
    match name:
        case "attributename":
            try:
                record = AttributeName.objects.get(id=id)
                serializer = AttributeNameSerializer(record,many=False)
                return Response(serializer.data)
            except AttributeName.DoesNotExist:
                return Response()

        case "attributevalue":
            try:
                record = AttributeValue.objects.get(id=id)
                serializer = AttributeValueSerializer(record,many=False)
                return Response(serializer.data)
            except AttributeValue.DoesNotExist:
                return Response()
        case "attribute":
            try:
                record = Attribute.objects.get(id=id)
                serializer = AttributeSerializer(record,many=False)
                return Response(serializer.data)
            except Attribute.DoesNotExist:
                return Response()
        case "product":
            try:
                record = Product.objects.get(id=id)
                serializer = ProductSerializer(record,many=False)
                return Response(serializer.data)
            except Product.DoesNotExist:
                return Response()
        case "productattributes":
            try:
                record = ProductAttributes.objects.get(id=id)
                serializer = ProductAttributesSerializer(record,many=False)
                return Response(serializer.data)
            except ProductAttributes.DoesNotExist:
                return Response()
        case "productimage":
            try:
                record = ProductImage.objects.get(id=id)
                serializer = ProductImageSerializer(record,many=False)
                return Response(serializer.data)
            except ProductImage.DoesNotExist:
                return Response()
        case "image":
            try:
                record = Image.objects.get(id=id)
                serializer = ImageSerializer(record,many=False)
                return Response(serializer.data)
            except Image.DoesNotExist:
                return Response()
        case "catalog":
            try:
                record = Catalog.objects.get(id=id)
                serializer = CatalogSerializer(record,many=False)
                return Response(serializer.data)
            except Catalog.DoesNotExist:
                return Response()
        case _:
            return Response()
        
@api_view(['POST'])
def importData(request):
    data = request.data
    try:
        for record in data:
            key, value = list(record.items())[0]
            newdata = json.dumps(value)
            new_d = json.loads(newdata)
            key = key.lower()
            match key:
                case "attributename":
                    try:
                        id_number = value['id']
                        record = AttributeName.objects.get(id = id_number)
                        serializer =AttributeNameSerializer(instance = record ,data = new_d)
                    except AttributeName.DoesNotExist:
                        serializer =AttributeNameSerializer(data = new_d)
                    finally:
                        if serializer.is_valid():
                            serializer.save()
                        Response(serializer.data)
                case "attributevalue":
                    try:
                        id_number = value['id']
                        record = AttributeValue.objects.get(id = id_number)
                        serializer =AttributeValueSerializer(instance = record ,data = new_d)
                    except AttributeValue.DoesNotExist:
                        serializer =AttributeValueSerializer(data = new_d)
                    finally:
                        if serializer.is_valid():
                            serializer.save()
                        Response(serializer.data)
                case "attribute":
                    try:
                        id_number = value['id']
                        record = Attribute.objects.get(id = id_number)
                        serializer =AttributeSerializer(instance = record ,data = new_d)
                    except Attribute.DoesNotExist:
                        serializer =AttributeSerializer(data = new_d)
                    finally:
                        if serializer.is_valid():
                            serializer.save()
                        Response(serializer.data)
                case "product":
                    try:
                        id_number = value['id']
                        record = Product.objects.get(id = id_number)
                        serializer =ProductSerializer(instance = record ,data = new_d)
                    except Product.DoesNotExist:
                        serializer =ProductSerializer(data = new_d)
                    finally:
                        if serializer.is_valid():
                            serializer.save()
                        Response(serializer.data)
                case "productattributes":
                    try:
                        id_number = value['id']
                        record = ProductAttributes.objects.get(id = id_number)
                        serializer =ProductAttributesSerializer(instance = record ,data = new_d)
                    except ProductAttributes.DoesNotExist:
                        serializer =ProductAttributesSerializer(data = new_d)
                    finally:
                        if serializer.is_valid():
                            serializer.save()
                        Response(serializer.data)
                case "productimage":
                    try:
                        id_number = value['id']
                        record = ProductImage.objects.get(id = id_number)
                        serializer =ProductImageSerializer(instance = record ,data = new_d)
                    except ProductImage.DoesNotExist:
                        serializer =ProductImageSerializer(data = new_d)
                    finally:
                        if serializer.is_valid():
                            serializer.save()
                        Response(serializer.data)
                case "image":
                    try:
                        id_number = value['id']
                        record = Image.objects.get(id = id_number)
                        serializer =ImageSerializer(instance = record ,data = new_d)
                    except Image.DoesNotExist:
                        serializer =ImageSerializer(data = new_d)
                    finally:
                        if serializer.is_valid():
                            serializer.save()
                        Response(serializer.data)
                case "catalog":
                    try:
                        id_number = value['id']
                        record = Catalog.objects.get(id = id_number)
                        serializer =CatalogSerializer(instance = record ,data = new_d)
                    except Catalog.DoesNotExist:
                        serializer =CatalogSerializer(data = new_d)
                    finally:
                        if serializer.is_valid():
                            serializer.save()
                        Response(serializer.data)
                case _:
                    return Response()
        return Response(request.data)
    except AttributeError:
        return Response()
        
    
        