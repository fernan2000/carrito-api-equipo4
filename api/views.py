from rest_framework import mixins, viewsets

from .models import Componente, HistorialDecision, TiempoReaccion
from .serializers import (
    ComponenteSerializer,
    HistorialDecisionSerializer,
    TiempoReaccionSerializer,
)


# ReadOnlyModelViewSet: solo GET (listar y detalle). POST/PUT/PATCH/DELETE devuelven 405.
class ComponenteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Componente.objects.all().order_by("nombre")
    serializer_class = ComponenteSerializer
    lookup_value_regex = "[^/]+"  # permite nombres con espacios, puntos, etc.


# GET (listar/detalle) + POST (el carrito guarda decisiones). Sin PUT/PATCH/DELETE.
class HistorialDecisionViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = HistorialDecision.objects.all().order_by("-id")
    serializer_class = HistorialDecisionSerializer


class TiempoReaccionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TiempoReaccion.objects.all().order_by("-id")
    serializer_class = TiempoReaccionSerializer