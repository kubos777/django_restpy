from django.urls import path
from api.apiviews import ProductoDetalle, ProductoList, \
    CategoriaList, SubCategoriaList, CategoriaDetalle, \
    SubCategoriaAdd, ProductoViewSet, UserCreate, \
    LoginView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls

schema_view = get_swagger_view(title='REST API Productos prrones')

#Se crea el router
router = DefaultRouter()
router.register('v2/productos', ProductoViewSet, base_name='productos')

urlpatterns = [
    path('v1/productos/', ProductoList.as_view(), name='productos_list'),
    path('v1/productos/<int:pk>', ProductoDetalle.as_view(), name='productos_detalle'),
    # path('v1/categorias/', CategoriaSave.as_view(),name='categoria_save' ),
    # path('v1/subcategorias/', SubCategoriaSave.as_view(),name='subcategoria_save' )
    path('v1/categorias/', CategoriaList.as_view(), name='categoria_list'),
    path('v1/subcategorias/', SubCategoriaList.as_view(), name='subcategoria_list'),
    path('v1/categorias/<int:pk>', CategoriaDetalle.as_view(),name='categoria_list'),
    path('v1/categorias/<int:pk>/subcategorias/', SubCategoriaList.as_view(),name='categoria_list'),
    path('v1/categorias/<int:cat_pk>/addsubcategorias/', SubCategoriaAdd.as_view(),name='subcategoria_apiview'),
    path('v3/usuarios/', UserCreate.as_view(), name='usuario_crear'),
    path("login/", LoginView.as_view(), name="login"),
    path("v3/login-drf/", views.obtain_auth_token, name="login_drf"),
    path('swagger/',schema_view),
    path('coreapi/',include_docs_urls(title='Documentación oficial COREAPI')),


]


urlpatterns += router.urls
