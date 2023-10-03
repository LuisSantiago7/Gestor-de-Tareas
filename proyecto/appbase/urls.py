from django.urls import path
from .views import listaPendientes, DetalleTarea, CrearTarea, EditarTarea, EliminarTarea, Login, RegistroUser
from django.contrib.auth.views import LogoutView

urlpatterns = [path('login-user/', Login.as_view(), name = 'login-user'),
               path('logout-user/', LogoutView.as_view(next_page= 'login-user'), name = 'logout-user'),
               path('register-user/', RegistroUser.as_view(), name = 'register-user'),
               path('', listaPendientes.as_view(), name='tareas'), 
               path('tarea/<int:pk>', DetalleTarea.as_view(), name='tarea'),
               path('crear-tarea/', CrearTarea.as_view(), name='crear-tarea'),
               path('editar-tarea/<int:pk>', EditarTarea.as_view(), name = 'editar-tarea'),
               path('eliminar-tarea/<int:pk>', EliminarTarea.as_view(), name= 'eliminar-tarea')]