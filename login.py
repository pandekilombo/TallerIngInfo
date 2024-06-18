from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from google.cloud import firestore
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud.firestore_v1.base_query import FieldFilter

from socket import create_connection, gaierror

from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.list import OneLineAvatarIconListItem
from kivy.properties import StringProperty
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.core.window import Window
from kivymd.uix.button import MDIconButton
from kivymd.uix.button import MDFlatButton
from kivy.properties import StringProperty, ObjectProperty
# Initialize Firebase Admin SDK
cred = credentials.Certificate('serviceAccountKey.json')
app = firebase_admin.initialize_app(cred)


# Crea un nuevo documento en Firestore
db = firestore.client()

doc_ref = db.collection("Usuarios").document("Miguel_Contreras1")
doc_ref2 = db.collection("Usuarios").document("m")
doc_ref3 = db.collection("Usuarios").document("m-no-admin")


doc_ref.set({"Nombre": "Miguel","Apellido1": "Contreras","Apellido2": "Fuentealba", "Contrasena": "1234", "Rol": "Admin"})
doc_ref2.set({"Nombre": "Miguel","Apellido1": "Contreras","Apellido2": "Fuentealba", "Contrasena": "2", "Rol": "Admin"})
doc_ref3.set({"Nombre": "Miguel","Apellido1": "Contreras","Apellido2": "Fuentealba", "Contrasena": "2", "Rol": "User"})

#Productos NO DESCOMENTAR - SE CREAN OBJETOS NUEVOS CON ID DISTINTA SI SE EJECUTAN


#Codigo extraido de la app movil, perdon diego
#---------------------------Elementos-------------------------#

class ListItemWithChip(OneLineAvatarIconListItem):
    # Elementos de lista personalizado
    icon = StringProperty("arm-flex")
    def __init__(self, **kwargs):
        super(ListItemWithChip, self).__init__(**kwargs)
        if self.text == 'Tasks':
            self.icon = StringProperty('arm-flex')
        elif self.text == 'Exercises':
            self.icon = StringProperty('arm-flex-outline')
        elif self.text == 'Streaks':
            self.icon = StringProperty('arm-flex')

    def get_icon(self):
        return self.icon

class InvalidLoginPopup(BoxLayout):
    # Abre un cuadro de diálogo cuando el usuario ingresa detalles inválidos al iniciar sesión
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

#Dialogo de error campos vacios

class ValidLoginPopup(BoxLayout):
    # Abre un cuadro de diálogo cuando el usuario ingresa detalles válidos al iniciar sesión
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class NoInternetPopup(BoxLayout):
    # Abre un cuadro de diálogo cuando no hay conexión a internet
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class EliminarUsuarioWidget(BoxLayout):
    def __init__(self, nombre_documento, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "horizontal"
        
        self.eliminar_button = MDIconButton(icon="trash-can-outline")
        self.eliminar_button.bind(on_release=lambda x: self.eliminar_usuario(nombre_documento))
        
        self.add_widget(self.eliminar_button)
    
    def eliminar_usuario(self, nombre_documento):
        # Aquí debes agregar la lógica para eliminar el usuario con el nombre del documento dado
        print(f"Eliminando usuario con nombre de documento: {nombre_documento}")

#---------------------Pantallas-------------------------------#

class MainWindow(MDScreen):
    # Pantalla principal
    def checkAdmin(self):
        print("aaa")
        return True
    
    def Test(self):
        print("Cargando Vehiculos")
        return True
    


class ContadorAutosInscritos():
    def __init__(self):
        self.Autos=0


    def AutoAñadido(self):
        self.Autos=self.Autos+1

    def Reiniciar(self):
        self.Autos=0

    def MostrarCantidad(self):
        print(self.Autos)

    def DameNumero(self):

        return self.Autos
    

ContadorDeAutos=ContadorAutosInscritos()



class Eliminar_Usuario(MDScreen):
    def eliminar(self):
        res = db.collection("Usuarios").document(self.ids.usuario.text).delete()  # delete document
        self.ids.usuario.text = ""
        print(res)

class BackUp():
    def __init__(self):
        self.UserID=""
    def SaveUserID(self,User):
        self.UserID=User
    def GiveUserID(self):
        return self.UserID
    
NewBackup=BackUp()


class Anadir_Usuario(MDScreen):
    def agregar(self):
        res = db.collection("Usuarios").document(self.ids.usuario.text).set({  # insert document
            'Nombre': self.ids.nombre.text,
            'Apellido1': self.ids.apellido_p.text,
            'Apellido2': self.ids.apellido_m.text,
            'Rol': self.ids.rol.text,                        
            'Contrasena': self.ids.password.text,
        })
        self.ids.usuario.text = ""
        self.ids.nombre.text = ""
        self.ids.apellido_p.text = ""
        self.ids.apellido_m.text = ""
        self.ids.rol.text = ""                
        self.ids.password.text = ""
        print(res)



class Anadir_Vehiculo(MDScreen):
    def agregar(self):
        pass

class Eliminar_Vehiculo(MDScreen):
    def eliminar(self):
        res = db.collection("Vehiculos").document(self.ids.id_prod.text).delete()  # delete document
        self.ids.id_prod.text = ""
        print(res)


class Reservar_Espacio(MDScreen):
    def agregar(self):
        res = db.collection("Espacios").document(self.ids.id_prod.text).set({  # insert document
            'Auto': self.ids.auto.text,
            'Espacio': self.ids.espacio.text,
            'Lugar': self.ids.lugar.text,
                                   
         
        })
        self.ids.id_prod.text = ""
        self.ids.auto.text = ""
        self.ids.espacio.text = ""
        self.ids.nlugar.text = ""
        print(res)

    
class Espacio_Reservado(MDScreen):
    def agregar(self):
        res = db.collection("Espacios").document(self.ids.id_prod.text).set({  # insert document
            'Auto': self.ids.auto.text,
            'Espacio': self.ids.espacio.text,
            'Lugar': self.ids.lugar.text,
                                   
         
        })
        self.ids.id_prod.text = ""
        self.ids.auto.text = ""
        self.ids.espacio.text = ""
        self.ids.nlugar.text = ""
        print(res)


class Espacios_Disponibles(MDScreen):
    def agregar(self):
        res = db.collection("Espacios").document(self.ids.id_prod.text).set({  # insert document
            'Auto': self.ids.auto.text,
            'Espacio': self.ids.espacio.text,
            'Lugar': self.ids.lugar.text,
                                   
         
        })
        self.ids.id_prod.text = ""
        self.ids.auto.text = ""
        self.ids.espacio.text = ""
        self.ids.nlugar.text = ""
        print(res)



class AdminWindow(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)    
    def build(self):
        # Crear instancia de MDDataTable
        pass

    def eliminar_filas_seleccionadas(self):
        print("test")

class Vehiculos(MDScreen):
    dialog = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)    
    def build(self):
        # Crear instancia de MDDataTable
 
        pass

    def close_dialog(self, *args):
        self.dialog.dismiss()    
    def Insertar_Auto(self,marca,modelo,anio,patente):
        if self.dialog.content_cls.ids.marca.text != "" and self.dialog.content_cls.ids.modelo.text !="" and self.dialog.content_cls.ids.anio.text != "" and self.dialog.content_cls.ids.patente.text !="":
            res = db.collection("Usuarios").document(NewBackup.GiveUserID()).collection("Vehiculos").document(patente).set({  # insert document
                'Marca': marca,
                'Modelo': modelo,
                'anio': anio,

                                    
            
            })             
            self.dialog.content_cls.ids.marca.text=""
            self.dialog.content_cls.ids.modelo.text=""
            self.dialog.content_cls.ids.anio.text=""
            self.dialog.content_cls.ids.patente.text=""
  
            print(res)
        else:
            self.Error()
            print("campos vacios")
    def LimpiarDialog(self):
        self.dialog=None


    def Añadir_Vehiculo(self):
        self.LimpiarDialog()
        if not self.dialog:
            self.dialog = MDDialog(
                title="Añadir Vehiculo:",
                type="custom",
                content_cls=Content(),
                buttons=[
                    MDFlatButton(
                        text="Cerrar",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.close_dialog,
                        
                    ),
                    MDFlatButton(
                        text="Ok",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.insertar_auto_from_content,
                    ),
                ],
            )
        self.dialog.open()


    def Quitar_Auto(self):

        self.LimpiarDialog()
        if not self.dialog:
            self.dialog = MDDialog(
                title="Eliminar Vehiculo:",
                type="custom",
                content_cls=Content2(),
                buttons=[
                    MDFlatButton(
                        text="Cerrar",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.close_dialog,
                        
                    ),
                    MDFlatButton(
                        text="Ok",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.quitar_auto_from_content,
                    ),
                ],
            )
        self.dialog.open()       




    def Error(self):
        self.close_dialog()
        self.LimpiarDialog()
        if not self.dialog:
            self.dialog = MDDialog(
                title="Campo Incorrecto",
                type="custom",
                content_cls=ErrorCampoVacio(),
                buttons=[
                    MDFlatButton(
                        text="Cerrar",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.close_dialog,
                        
                    ),
                ],
            )
        self.dialog.open()   

    def Success(self):
        # Correcto
        self.close_dialog()
        self.LimpiarDialog()
        if not self.dialog:
            self.dialog = MDDialog(
                title="Accion Existosa",
                type="custom",
                content_cls=Correcto(),
                buttons=[
                    MDFlatButton(
                        text="Cerrar",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.close_dialog,
                        
                    ),
                ],
            )
        self.dialog.open()   

    def Quitar_Auto2(self,Auto):
        res = db.collection("Usuarios").document(str(NewBackup.GiveUserID())).collection("Vehiculos").document(Auto).delete()  # delete document
        self.dialog.content_cls.ids.Auto_Borrar.text=""
        self.close_dialog()
        self.LimpiarDialog()        
        print(res)        


    def quitar_auto_from_content(self, *args):
        if self.dialog.content_cls.ids.Auto_Borrar.text != "" :
            Auto = self.dialog.content_cls.ids.Auto_Borrar.text
            self.Quitar_Auto2(Auto)
        else: 
            print("Campo Vacio")
      
            self.Error()        
    def Actualizar_Auto(self):
        self.LimpiarDialog()
        if not self.dialog:
            self.dialog = MDDialog(
                title="Actualizar Vehiculo",
                type="custom",
                content_cls=Content3(),
                buttons=[
                    MDFlatButton(
                        text="Cerrar",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.close_dialog,
                    ),
                    MDFlatButton(
                        text="Ok",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.Actualizar_auto_from_content,
                    ),
                ],
            )
        self.dialog.open()             




    def Actualizar_Auto2(self,marca,modelo,anio,patente):
        if self.dialog.content_cls.ids.marca.text != "" and self.dialog.content_cls.ids.modelo.text !="" and self.dialog.content_cls.ids.anio.text != "" and self.dialog.content_cls.ids.patente.text !="":
            res = db.collection("Usuarios").document(NewBackup.GiveUserID()).collection("Vehiculos").document(patente).update({  # insert document
                'Marca': marca,
                'Modelo': modelo,
                'anio': anio,
                


            
            })        
            self.dialog.content_cls.ids.marca.text=""
            self.dialog.content_cls.ids.modelo.text=""
            self.dialog.content_cls.ids.anio.text=""
            self.dialog.content_cls.ids.patente.text=""
            
            print(res)
        else:
            self.Error()            
            print("campos vacios o no encontrado")        


    def Actualizar_auto_from_content(self, *args):

        marca = self.dialog.content_cls.ids.marca.text
        modelo = self.dialog.content_cls.ids.modelo.text
        anio = self.dialog.content_cls.ids.anio.text
        patente = self.dialog.content_cls.ids.patente.text

        self.Actualizar_Auto2(marca, modelo, anio, patente)

    def insertar_auto_from_content(self, *args):
        marca = self.dialog.content_cls.ids.marca.text
        modelo = self.dialog.content_cls.ids.modelo.text
        anio = self.dialog.content_cls.ids.anio.text
        patente = self.dialog.content_cls.ids.patente.text

        self.Insertar_Auto(marca, modelo, anio, patente)

class Content(BoxLayout):
    pass

class Content2(BoxLayout):
    pass

class Content3(BoxLayout):
    pass
class ErrorCampoVacio(BoxLayout):
    pass


class Correcto(BoxLayout):
    pass


class LoginScreen(MDScreen):
    # Pantalla de inicio de sesión
    Admin=False

    def checkUser(self, user, password):
        # Comprueba si el usuario y la contraseña son correctos
        if not user or not password:
            return False
        else:
            data = db.collection('Usuarios').document(user)
            users = data.get()
            if not users.exists:
                return False
            passw = users.to_dict().get('Contrasena')
            return password == passw

    def comprobarConexion(self):
        # Comprueba si hay conexión a internet
        try:
            create_connection(("www.google.com", 80))
            return True
        except gaierror:
            return False

    def login(self):
        # Inicia sesión
        if self.ids.user.text and self.ids.password.text:
            user = self.ids.user.text
            password = self.ids.password.text
          #  if self.ids.keepmeloggedin.active == True:
          #      keepMeLogged = True
          #  else:
          #      keepMeLogged = False
            if self.comprobarConexion() == True:
                print("test")
                
                #PROBLEMA
                if self.checkUser(user, password) == True:
                    NewBackup.SaveUserID(user)
                    print(NewBackup.GiveUserID())
                    return True
                else:
                    self.invalidPopup()
            else:
                self.noInternetPopup()
        else:
            self.invalidPopup()


    def invalidPopup(self):
        # Cuadro de diálogo para entradas inválidas
        self.dialog = MDDialog(
                type="custom",
                content_cls= InvalidLoginPopup(),
                size_hint=(.4, .4),
                auto_dismiss=True,
            )
        self.dialog.open()

    def validPopup(self):
        # Cuadro de diálogo para entradas válidas
        self.dialog = MDDialog(
                type="custom",
                content_cls= ValidLoginPopup(),
                size_hint=(.4, .4),
                auto_dismiss=True,
            )
        self.dialog.open()

    def noInternetPopup(self):
        # Cuadro de diálogo para cuando no hay conexión a internet
        self.dialog = MDDialog(
                type="custom",
                content_cls= NoInternetPopup(),
                size_hint=(.4, .4),
                auto_dismiss=True,
            )
        self.dialog.open()

class RecoverPasswordScreen(MDScreen):
    def invalidPopup(self):
        # Cuadro de diálogo para entradas inválidas
        self.dialog = MDDialog(
                type="custom",
                content_cls= InvalidLoginPopup(),
                size_hint=(.4, .4),
                auto_dismiss=True,
            )
        self.dialog.open()

    def noInternetPopup(self):
        # Cuadro de diálogo para cuando no hay conexión a internet
        self.dialog = MDDialog(
                type="custom",
                content_cls= NoInternetPopup(),
                size_hint=(.4, .4),
                auto_dismiss=True,
            )
        self.dialog.open()

class ScreenManagement(ScreenManager):
    pass
class NavDrawer(BoxLayout):
    # Panel de navegación
    manager = ObjectProperty()
    nav_drawer = ObjectProperty()





    



#Creacion de la APP
class MainApp(MDApp):
    
    #Base de la app
    def build(self):
        Window.size = (260, 500)
        #Configuracion visual inicial
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"

        
        #Creacion de la pantalla con el archivo .kv externo
        return Builder.load_file('login.kv')



    def switchWindow(self, window, boolean_val):
     if boolean_val:
        if window == "login":
            # Limpiar los campos de usuario y contraseña al cambiar a la ventana de inicio de sesión
            self.root.get_screen('login').ids.user.text = ''
            self.root.get_screen('login').ids.password.text = ''
        self.root.current = window
        self.root.transition.direction = "down"





        if window == "adminwindow":
            # Obtener una referencia a la colección en Firestore

            docs_ref = db.collection("Usuarios")

            # Recuperar todos los documentos en la colección
            docs = docs_ref.stream()

            # Crear una lista para almacenar los datos
            data = []

            # Iterar sobre los documentos y extraer los datos
            for doc in docs:
                user_data = doc.to_dict()
                nombre_documento = doc.id
                apellido1 = user_data.get("Apellido1", "")
                apellido2 = user_data.get("Apellido2", "")
                contrasena = user_data.get("Contrasena", "")
                nombre = user_data.get("Nombre", "")
                rol = user_data.get("Rol", "")


                data.append((nombre_documento, nombre, apellido1, apellido2, contrasena, rol))
            


            self.root.get_screen('adminwindow').ids.container.clear_widgets()
            self.root.get_screen('adminwindow').ids.container.add_widget(MDDataTable(
                pos_hint={'center_x': 0.5, 'center_y': 0.5},
                size_hint=(1, 1),
                check=False,
                use_pagination=True,
                rows_num=len(data),
                column_data=[
                    ("Usuario", dp(40)),
                    ("Nombre", dp(20)),                    
                    ("Apellido1", dp(20)),
                    ("Apellido2", dp(20)),
                    ("Contraseña", dp(20)),
                    ("Rol", dp(15))
                 
                ],  # Definir las columnas
                row_data=data  # Pasar los datos recuperados directamente
                
            ))

        if window == "vehwindow":
            

            #PARA EXTRAER LOS DATOS


            
            # Obtener una referencia a la colección en Firestore
            
            docs_ref = db.collection('Usuarios').document(NewBackup.GiveUserID()).collection('Vehiculos')

            #Contador de autos registrados en la cuenta
            ContadorDeAutos.Reiniciar()

            # Recuperar todos los documentos en la colección
            docs = docs_ref.stream()

            # Crear una lista para almacenar los datos
            data = []

            # Iterar sobre los documentos y extraer los datos
            for doc in docs:
                user_data = doc.to_dict()
                nombre_documento = doc.id
                Marca = user_data.get("Marca","")
                Modelo= user_data.get("Modelo","")
                Anio= user_data.get("anio","")

                ContadorDeAutos.AutoAñadido()

                data.append((Marca, Modelo, Anio,nombre_documento))
            ContadorDeAutos.MostrarCantidad()
           # print("Datos: \n")
            print(data)
            if len(data)>=1:
                self.root.get_screen('vehwindow').ids.container.clear_widgets()
                self.root.get_screen('vehwindow').ids.container.add_widget(MDDataTable(
                    pos_hint={'center_x': 0.5, 'center_y': 0.7},
                    size_hint=(1, 1),
                    check=False,
                    use_pagination=True,
                    rows_num=len(data),
                    column_data=[
             
                        ("Marca", dp(20)),
                        ("Modelo", dp(20)),
                        ("Año", dp(20)),
                        ("Patente", dp(15))
                    
                    ],  # Definir las columnas
                    row_data=data  # Pasar los datos recuperados directamente
                    
                ))                
            else:
                print("No hay autos registrados")
            



MainApp().run()