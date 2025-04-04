from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.base.views import HomeViewSet, Catalogs_ElectronicLibraryViewSet, WeOfferViewingView, PartnersView, ReadingRatingView, BooksRatingView
from app.base.search import GlobalSearch, Similars


router = DefaultRouter()

#Саидахмад
router.register(r'logo', HomeViewSet, basename='logo')
router.register(r'catalogs_electroniclibrary', Catalogs_ElectronicLibraryViewSet, basename='catalogs_electroniclibrary')

#Алишер 
router.register(r'weofferviewing', WeOfferViewingView, basename='weofferviewing')
router.register(r'partners', PartnersView, basename='partners')
router.register(r'readingrating', ReadingRatingView, basename='readingrating')
router.register(r'booksrating', BooksRatingView, basename='booksrating')



urlpatterns = [
    path('', include(router.urls)),
    path('search/', GlobalSearch.as_view(), name='global-search'),
    path('similars/', Similars.as_view(), name='similars'),
]