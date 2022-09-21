
from django.http import HttpResponse
from django.template import Template , Context
from django.shortcuts import render

# Create your views here.
def index(request):
        return render(request,'index.html')

def juguete(request):
    context = {
        'data' :[
            {
                "img" : "image/111.jpg",
                "nombre" : "Max Steel",
                "precio" : "9.990",
                "desc"  :  "Incluye pilas",
                "categoria" : "JUGUETES"
            },
            {
                "img" : "image/222.jpg",
                "nombre" : "Funko pop Dr Octopus",
                "precio" : "12.990",
                "desc"  :  "Edición especial ",
                "categoria" : "JUGUETES"
            },
            {
                "img" : "image/333.jpg",
                "nombre" : "Spiderman articulado",
                "precio" : "19.990",
                "desc"  :  "Edición coleccionista",
                "categoria" : "JUGUETES"
            }
        ]
    }
    return render(request,'vistaPlantilla.html',context)

def ropa(request):
    context = {
        'data' :[
            {
                "nombre" : "Polera Nike ",
                "precio" : "29.990",
                "desc"  :  "Talla M",
                "img" : "image/444.jpg",
                "categoria" : "ROPA"
            },
            {
                "nombre" : "Jeans azul Bearcliff hombre ",
                "precio" : "14.990",
                "desc"  :  "Talla S",
                "img" : "image/555.jpg",
                "categoria" : "ROPA"
            },
            {
                "nombre" : "Short hombre Adidas ",
                "precio" : "24.990",
                "desc"  :  "Talla L",
                "img" : "image/666.jpg",
                "categoria" : "ROPA"
            }
        ]
    }
    return render(request,'vistaPlantilla.html',context)

def infousuario(request):   #Vista usuario con HttpResponse

    nombre_usuario="Fabian"
    apellido_usuario="Collao"
    email_usuario="fabiancollao@gmail.com"
    id_usuario="777"
    numero_usuario="+56911122233"

    doc_externo=open("C:/Users/fabia/Documents/back end/Django_Evaluacion_1/plantillas/userinfotemplate.html")
    temp=Template(doc_externo.read())
    doc_externo.close()

    contexto=Context({"nombre":nombre_usuario,"apellido":apellido_usuario,"id":id_usuario,"email":email_usuario,"numero":numero_usuario})
    documento=temp.render(contexto)


    return HttpResponse(documento)