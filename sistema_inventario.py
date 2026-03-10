class Producto:
    """Clase que representa un producto del inventario"""
    
    def __init__(self, nombre, precio, cantidad):
        # Validar tipo de dato para nombre
        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser una cadena de texto (str)")
        
        # Validar que el nombre no este vacio
        if not nombre.strip():
            raise ValueError("El nombre del producto no puede estar vacio")
        
        # Validar tipo de dato para precio
        if not isinstance(precio, (int, float)):
            raise TypeError("El precio debe ser un numero (int o float)")
        
        # Validar que el precio sea mayor o igual a cero
        if precio < 0:
            raise ValueError("El precio debe ser mayor o igual a cero")
        
        # Validar tipo de dato para cantidad
        if not isinstance(cantidad, int):
            raise TypeError("La cantidad debe ser un numero entero (int)")
        
        # Validar que la cantidad sea mayor o igual a cero
        if cantidad < 0:
            raise ValueError("La cantidad debe ser mayor o igual a cero")
        
        self.nombre = nombre.strip()
        self.precio = float(precio)
        self.cantidad = cantidad
    
    def actualizar_precio(self, nuevo_precio):
        if not isinstance(nuevo_precio, (int, float)):
            raise TypeError("El precio debe ser un numero (int o float)")
        
        if nuevo_precio < 0:
            raise ValueError("El precio debe ser mayor o igual a cero")
        
        self.precio = float(nuevo_precio)
    
    def actualizar_cantidad(self, nueva_cantidad):
        if not isinstance(nueva_cantidad, int):
            raise TypeError("La cantidad debe ser un numero entero (int)")
        
        if nueva_cantidad < 0:
            raise ValueError("La cantidad debe ser mayor o igual a cero")
        
        self.cantidad = nueva_cantidad
    
    def calcular_valor_total(self):
        return self.precio * self.cantidad
    
    def __str__(self):
        return f"Nombre: {self.nombre} | Precio: ${self.precio:.2f} | Cantidad: {self.cantidad} | Valor Total: ${self.calcular_valor_total():.2f}"


class Inventario:
    """Clase que gestiona una coleccion de productos"""
    
    def __init__(self):
        """Inicializa un inventario vacio"""
        self.productos = []
    
    def agregar_producto(self, producto):
        if not isinstance(producto, Producto):
            raise TypeError("El objeto debe ser una instancia de la clase Producto")
        
        self.productos.append(producto)
    
    def buscar_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                return producto
        
        return None
    
    def calcular_valor_inventario(self):
        return sum(producto.calcular_valor_total() for producto in self.productos)
    
    def listar_productos(self):
        if not self.productos:
            print("\nEl inventario esta vacio.")
            return
    
        print("LISTADO DE PRODUCTOS DEL INVENTARIO")
        
        for indice, producto in enumerate(self.productos, 1):
            print(f"{indice}. {producto}")



def obtener_entrada_float(mensaje):
    try:
        valor = input(mensaje)
        if valor.lower() == 'cancelar':
            return None
        return float(valor)
    except ValueError:
        print("Error: Debe ingresar un numero valido.")
        return None


def obtener_entrada_entero(mensaje):
    try:
        valor = input(mensaje)
        if valor.lower() == 'cancelar':
            return None
        return int(valor)
    except ValueError:
        print("Error: Debe ingresar un numero entero valido.")
        return None


def menu_principal():
    inventario = Inventario()
    
    while True:
        print("\n")
        print("SISTEMA DE INVENTARIO")
        print("\n")
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Listar productos")
        print("4. Calcular valor total del inventario")
        print("5. Salir")
        print("\n")
        
        opcion = input("Seleccione una opcion (1-5): ").strip()
        
        try:
            if opcion == '1':
                # Agregar producto
                print("\n--- AGREGAR PRODUCTO ---")
                nombre = input("Nombre del producto (o 'cancelar' para volver): ").strip()
                
                if nombre.lower() == 'cancelar':
                    continue
                
                precio = obtener_entrada_float("Precio del producto (o 'cancelar' para volver): ")
                if precio is None:
                    continue
                
                cantidad = obtener_entrada_entero("Cantidad del producto (o 'cancelar' para volver): ")
                if cantidad is None:
                    continue
                
                producto = Producto(nombre, precio, cantidad)
                inventario.agregar_producto(producto)
                print(f"Producto '{nombre}' agregado exitosamente al inventario.")
            
            elif opcion == '2':
                # Buscar producto
                print("\n--- BUSCAR PRODUCTO ---")
                nombre = input("Ingrese el nombre del producto a buscar (o 'cancelar' para volver): ").strip()
                
                if nombre.lower() == 'cancelar':
                    continue
                
                producto = inventario.buscar_producto(nombre)
                
                if producto:
                    print(f"\nProducto encontrado:")
                    print(producto)
                else:
                    print(f"Error: No se encontro ningun producto con el nombre '{nombre}'.")
            
            elif opcion == '3':
                # Listar productos
                inventario.listar_productos()
            
            elif opcion == '4':
                # Calcular valor total del inventario
                valor_total = inventario.calcular_valor_inventario()
                print(f"\nValor total del inventario: ${valor_total:.2f}")
            
            elif opcion == '5':
                # Salir
                print("\nGracias por usar el sistema de inventario. Hasta luego.")
                break
            
            else:
                print("Error: Opcion no valida. Por favor, seleccione una opcion entre 1 y 5.")
        
        except ValueError as e:
            print(f"Error de validacion: {e}")
        except TypeError as e:
            print(f"Error de tipo: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")


if __name__ == "__main__":
    menu_principal()
