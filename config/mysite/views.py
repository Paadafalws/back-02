from django.shortcuts import render
from mysite.serializers import QuadroSerializer
from rest_framework import viewsets
from mysite.models import Quadro
from mysite.serializers import Quadro
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import UpdateAPIView
from rest_framework import filters


class QuadrosViewSet(viewsets.ModelViewSet):
    "sdaasd"
    queryset = Quadro.objects.all()
    serializer_class = QuadroSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['Nome', 'Quadro']



class EditarQuadroView(UpdateAPIView):
    """Editar na api"""
    queryset = Quadro.objects.all()
    serializer_class = QuadroSerializer

    def get_object(self):
        # Obtém o Quadro com base no parâmetro pk da URL
        pk = self.kwargs['pk']
        return Quadro.objects.get(pk=pk)
    
class CustomSearchFilter(filters.SearchFilter):
    # barra de pesquisa
    def get_search_fields(self, view, request):
        if request.query_params.get('Nome'):
            return ['Nome']
        return super().get_search_fields(view, request)


@api_view(['POST'])
def adicionar_quadros(request):
    if request.method == 'POST':
        serializer = QuadroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

@api_view(['PUT'])
def atualizar_quadros(request, pk):
    try:
        aluno = Quadro.objects.get(pk=pk)
    except Quadro.DoesNotExist:
        return Response({"error": "Aluno não encontrado."}, status=404)

    if request.method == 'PUT':
        # Remove o campo 'foto' do dicionário request.data
        request.data.pop('foto', None)

        serializer = QuadroSerializer(Quadro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)