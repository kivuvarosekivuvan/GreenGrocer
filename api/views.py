from django.shortcuts import render
from rest_framework.views import APIView
from customer.models import Customer 
from .serializer import CustomerSerializer
from rest_framework.response import Response
from rest_framework import status


# class CustomerListView(APIView):
#     def get(self,request):
#         customers= Customer.objects.all()                   #This is querying
#         serializer =CustomerSerializer(customers, many=True)
#         return Response(serializer.data)
  

#     def post(self,request):
#         serializer =CustomerSerializer(data= request.data)                      #This is deserializing
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status =status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)    


# class CustomerDetailView(APIView):
#     def get(self,request, id, format=None):
#         customer= Customer.objects.all(id=id)                   
#         serializer =CustomerSerializer(customer, many=True)
#         return Response(serializer.data)

#     def put(self,request):
#         customer= Customer.objects.all(id=id)
#         serializer= CustomerSerializer(Customer, request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)    

#     def delete(self, request, id, format= None):
#         customer =Customer.objects.get(id=id)
#         customer.delete()
#         return Response('Customer deleted' ,status= status.HTTP_204_NO_CONTENT)




class CustomerListView(APIView):
    def get(self, request):
        customers = Customer.objects.all()  
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class CustomerDetailView(APIView):
    def get(self,request,id,format=None):
        customer=Customer.objects.get(id=id)
        serializer=CustomerSerializer(customer)
        return Response(serializer.data)
    def put(self,request,id,format=None):
        customer=Customer.objects.get(id=id)
        serializer=CustomerSerializer(customer,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id,format=None):
        customer=Customer.objects.get(id=id)
        customer.delete()
        return Response("customer successfully deleted",status=status.HTTP_204_NO_CONTENT)


    # inventory
class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()  # Corrected variable name
        serializer = InventorySerializer(products, many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=InventorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    


class  ProductDetailView(APIView):
    def get(self,request,id,format=None):
        product= Product.objects.get(id=id)
        serializer=InventorySerializer( product)
        return Response(serializer.data)
    
    def put(self,request,id,format=None):
        product= Product.objects.get(id=id)
        serializer=InventorySerializer(product,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id,format=None):
        product= Product.objects.get(id=id)
        product.delete()
        return Response("product successfully deleted",status=status.HTTP_204_NO_CONTENT)
    
# ###########################ORDER####################
class OrderListView(APIView):
    def get(self, request):
        order = Order.objects.all()  # Corrected variable name
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer= OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    


class  OrderDetailView(APIView):
    def get(self,request,id,format=None):
        order= Order.objects.get(id=id)
        serializer=OrderSerializer( order)
        return Response(serializer.data)
    
    def put(self,request,id,format=None):
        order= Order.objects.get(id=id)
        serializer= OrderSerializer(order,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id,format=None):
        order= Order.objects.get(id=id)
        order.delete()
        return Response("order successfully deleted",status=status.HTTP_204_NO_CONTENT)
    
# # ###########################.......CART...........####################
class CartListView(APIView):
    def get(self, request):
        cart = ShoppingCart.objects.all()  # Corrected variable name
        serializer = ShoppingCartSerializer(cart, many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=ShoppingCartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    


class  CartDetailView(APIView):
    def get(self,request,id,format=None):
        cart = ShoppingCart.objects.get(id=id)
        serializer=ShoppingCartSerializer(cart)
        return Response(serializer.data)
    
    def put(self,request,id,format=None):
        cart = ShoppingCart.objects.get(id=id)
        serializer= ShoppingCartSerializer(cart,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id,format=None):
        cart = ShoppingCart.objects.get(id=id)
        cart.delete()
        return Response("cart successfully deleted",status=status.HTTP_204_NO_CONTENT)
    
    def post(self, request, id, format=None):
        cart = ShoppingCart.objects.get(id=id)
        product_id = request.data.get('product_id')
        product = Product.objects.get(id=product_id)
        cart.products.add(product)
        serializer = ShoppingCartSerializer(cart)
        return Response(serializer.data, status=status.HTTP_200_OK)