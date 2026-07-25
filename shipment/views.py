from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from .serializers import OrderItemSerializer , ProductSerializer ,BoxSerializer
from .services import recommend_box
from .models import Product, ShippingBox


class RecommendBoxAPIView(APIView):
    def post(self , request):
        serializer = OrderItemSerializer(
            data = request.data['items'],
            many=True
        )
        serializer.is_valid(raise_exception=True)
        
        box= recommend_box(serializer.validated_data)
        
        if box is None:
            return Response({"message": "No suitable box found"})
        
        return Response({
            'box':box.name ,
            'cost':box.cost,
            'dimensions':[
                box.inner_length,
                box.inner_width,
                box.inner_height
            ]
        })
        

class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class BoxListAPIView(generics.ListAPIView):
    queryset = ShippingBox.objects.all()
    serializer_class = BoxSerializer
        