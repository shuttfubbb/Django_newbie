from django.urls import path
from rest_framework.routers import DefaultRouter
from product.views import ProductViewSet, bookSearchApi, ProductCreateView, ProductUpdateView, ProductDeleteView

router = DefaultRouter()
router.register(r'procducts', ProductViewSet)

urlpatterns = [
    path('procducts/', ProductViewSet.as_view({'get': 'list'}), name='procduct-list'),
    path('procducts/<int:pk>/', ProductViewSet.as_view({'get': 'retrieve'}), name='procduct-detail'),
    path('procducts/create/', ProductCreateView.as_view(), name='procduct-create'),
    path('procducts/<int:pk>/update/', ProductUpdateView.as_view(), name='procduct-update'),
    path('procducts/<int:pk>/delete/', ProductDeleteView.as_view(), name='procduct-destroy'),
    path('procducts/search', bookSearchApi, name="product-search")
]

urlpatterns += router.urls