from django.shortcuts import render
from hotel_app.filter import RoomFilter
from permissions.decorator import permission_required
from . models import Employee
from django.shortcuts import render,HttpResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
#from .blog_serializer import BlogSerializer
from utils.base_authentication import JWTAuthentication
from .hotel_controller import ContactController, EmployeeController, PublicBookingController, PublicRoomController, RoomController, GuestController, BookingController, PaymentController


employee_controller = EmployeeController()
guest_controller = GuestController()
room_controller = RoomController()
publicroom_controller = PublicRoomController()
booking_controller = BookingController()
publicbooking_controller = PublicBookingController()
payment_controller = PaymentController()
contact_controller = ContactController()
# bookingroom_controller = BookingRoomController()


class EmployeeViews(ModelViewSet):
    authentication_classes = [JWTAuthentication]

    @permission_required(['create_employee'])
    def post_employee(self, request):
        return employee_controller.create(request)
    
    @permission_required(['read_employee'])
    def get_employee(self, request):
        return employee_controller.get_employee(request)

    @permission_required(['update_employee'])
    def update_employee(self, request):
        return employee_controller.update_employee(request)

    @permission_required(['delete_employee'])
    def delete_employee(self, request):
        return employee_controller.delete_employee(request)
    
class GuestViews(ModelViewSet):
    # authentication_classes = [JWTAuthentication]

    def post_guest(self, request):
        return guest_controller.create_guest(request)
    
    def get_guest(self, request):
        return guest_controller.get_guest(request)
    
    def update_guest(self, request):
        return guest_controller.update_guest(request)
    
    def delete_guest(self, request):
        return guest_controller.delete_guest(request)
    
class RoomViews(ModelViewSet):
    authentication_classes = [JWTAuthentication]

    @permission_required(['create_room'])
    def post_room(self, request):
        return room_controller.create(request)
    
    @permission_required(['read_room'])
    def get_room(self, request):
        return room_controller.get_room(request)
    
    @permission_required(['update_room'])
    def update_room(self, request):
        return room_controller.update_room(request)
    
    @permission_required(['delete_room'])
    def delete_room(self, request):
        return room_controller.delete_room(request)
    
class PublicRoomViews(ModelViewSet):
    # authentication_classes = [JWTAuthentication]

    def get_publicroom(self, request):
        return publicroom_controller.get_publicroom(request)
  

class BookingViews(ModelViewSet):
    authentication_classes = [JWTAuthentication]

    @permission_required(['create_booking'])
    def post_booking(self, request):
        return booking_controller.create(request)
    
    @permission_required(['read_booking'])
    def get_booking(self, request):
        return booking_controller.get_booking(request)
    
    @permission_required(['update_booking'])
    def update_booking(self, request):
        return booking_controller.update_booking(request)
    
    @permission_required(['delete_booking'])
    def delete_booking(self, request):
        return booking_controller.delete_booking(request)

class PublicBookingViews(ModelViewSet):
    # authentication_classes = [JWTAuthentication]
    
    def post_publicbooking(self, request):
        return publicbooking_controller.post_publicbooking(request)   
    
class PaymentViews(ModelViewSet):
    authentication_classes = [JWTAuthentication]

    def post_payment(self, request):
        return payment_controller.create(request)
    
    def get_payment(self, request):
        return payment_controller.get_payment(request)

    def update_payment(self, request):
        return payment_controller.update_payment(request)

    def delete_payment(self, request):
        return payment_controller.delete_payment(request)
    
class ContactViews(ModelViewSet):
    authentication_classes = [JWTAuthentication]

    def post_contact(self, request):
        return contact_controller.create(request)

    def get_contact(self, request):
        return contact_controller.get_contact(request)
    
# class BookingViewSet(ModelViewSet):
#     authentication_classes = [JWTAuthentication]

#     def post_bookroom(self, request):
#         return bookingroom_controller.post_bookroom(request)