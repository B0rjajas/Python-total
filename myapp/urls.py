from django.urls import path 
from .views import ListaPendientes, DetalleTarea, CrearTarea, EditarTarea, EliminarTarea, Logueo, PaginaRegistro
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', Logueo.as_view(), name='login'),  # Ruta básica para la vista 'Logueo'
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),  # Ruta básica para la vista 'Logueo'
    path('registro/', PaginaRegistro.as_view(), name='registro'),  # Ruta básica para la vista 'Logueo'

    path('', ListaPendientes.as_view(), name='tareas'),  # Ruta básica para la vista 'index'
    path('tarea/<int:pk>/', DetalleTarea.as_view(), name='tarea'),  # Ruta básica para la vista 'tarea'
    path('crear-tarea/', CrearTarea.as_view(), name='crear-tarea'),  # Ruta básica para la vista 'tarea'
    path('editar-tarea/<int:pk>/', EditarTarea.as_view(), name='editar-tarea'),  # Ruta básica para la vista 'tarea'
    path('eliminar-tarea/<int:pk>/', EliminarTarea.as_view(), name='eliminar-tarea'),  # Ruta básica para la vista 'tarea'
]
