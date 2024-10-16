
from flask import Flask, jsonify, request
import mysql.connector

#Conexión con el servidor MySQL Server

app = Flask(__name__)

#@app.route('/Pedidos')
#def pedidos():
#    conexionMySQL = mysql.connector.connect(
#        host='10.9.120.5',
#        user='kmill',
#        passwd='kmill111',
#        db='kmill'
#    )
#    #Consulta SQL que ejecutaremos, en este caso un select
#    sqlSelect = """SELECT * FROM Pedido""" 
#    #Establecemos un db para la conexión con el servidor MySQL
#    db = conexionMySQL.cursor()
#    #A partir del db, ejecutamos la consulta SQL
#    db.execute(sqlSelect)
#    #Guardamos el resultado de la consulta en una variable
#    resultadoSQL = db.fetchall()
#
#    #Cerramos el db y la conexión con MySQL
#    db.close()
#    conexionMySQL.close()
#    return jsonify(resultadoSQL)




@app.route('/jsonproducto')
def producto():
    conexionMySQL = mysql.connector.connect(
        host='10.9.120.5',
        user='kmill',
        passwd='kmill111',
        db='kmill'
    )
    
<<<<<<< HEAD
    result = {"pedido": nropedido, "detalle pedido": detalle_pedido }
    return jsonify(result)



@app.route('/jsonproducto')
def producto():
=======
>>>>>>> 90d04689c69db783a19ba251fe17d67e17931857
    sqlSelect = """SELECT * FROM Producto"""
    cursor = conexionMySQL.cursor()
    cursor.execute(sqlSelect)
    resultadoSQL = cursor.fetchone()
    cursor.close()
    conexionMySQL.close()
    return jsonify(resultadoSQL)

@app.route('/producto/<int:id>') 
def detalle_producto(id):
    conexionMySQL = mysql.connector.connect(
        host='10.9.120.5',
        user='kmill',
        passwd='kmill111',
        db='kmill'
    ) 

    sqlSelect = """SELECT Nombre, Descripción, Precio, stock FROM Producto WHERE id = %s"""
    cursor = conexionMySQL.cursor()
    cursor.execute(sqlSelect, (id,))
    resultadoSQL = cursor.fetchone()

    cursor.close()
    conexionMySQL.close()
    return jsonify(resultadoSQL)


@app.route('/categoria/<int:id>') 
def detalle_categoria(id):
    conexionMySQL = mysql.connector.connect(
        host='10.9.120.5',
        user='kmill',
        passwd='kmill111',
        db='kmill'
    )

    sqlSelect = """SELECT Nombre FROM Categoria WHERE id = %s"""
    cursor = conexionMySQL.cursor()
    cursor.execute(sqlSelect, (id,))
    resultadoSQL = cursor.fetchone()

    cursor.close()
    conexionMySQL.close()
    return jsonify(resultadoSQL)

@app.route('/producto_ingrediente/<int:id>') 
def producto_ingrediente(id):
    conexionMySQL = mysql.connector.connect(
        host='10.9.120.5',
        user='kmill',
        passwd='kmill111',
        db='kmill'
    )

    #consulta 1
    qProducto = """SELECT Nombre FROM Producto WHERE id = %s"""
    cursor = conexionMySQL.cursor()
    cursor.execute(qProducto, (id,))
    product = cursor.fetchone()
    
   # SELECT i.Nombre from Ingrediente i 
    #INNER join Ingredientes_Productos ip ON i.id = ip.id_Ingredientes
    #INNER JOIN Producto p ON ip.id_Producto = p.id
    #WHERE ip.id_Ingredientes = 3
    #consulta 2
    qIngrediente = """ SELECT Nombre FROM Ingrediente WHERE id = %s """
    cursor.execute(qIngrediente, (id,))
    ingrediente = cursor.fetchall()
    
    cursor.close()

    resul = {  "nombre_pro": product[0],  # Nombre del producto
            "ingredientes":  [ingredient[0] for ingredient in ingrediente] }
    return jsonify(resul)

#       "Producto": product,
            #"Ingredientes": ingrediente 
<<<<<<< HEAD

=======
>>>>>>> 90d04689c69db783a19ba251fe17d67e17931857
@app.route('/Pedido', methods = ('PUT',))
def detalle_pedido(id):
    conexionMySQL = mysql.connector.connect(
        host='10.9.120.5',
        user='kmill',
        passwd='kmill111',
        db='kmill'
    )
    #Consulta 1
    qpedido = """SELECT id FROM Pedidos WHERE id = %s"""
    db = conexionMySQL.cursor(dictionary=True)
    db.execute(qpedido, (id,))
    nropedido = db.fetchone()['id']

    #Consulta 2
    qdetalle_pedido = """SELECT * FROM Detalle_pedido WHERE id = %s"""
    db.execute(qdetalle_pedido, (id,))
    detalle_pedido = list(db)

    #Cerramos el db y la conexión con MySQL
    db.close()
    conexionMySQL.close()
    
    result = {"pedido": nropedido, "detalle pedido": detalle_pedido }
    return jsonify(result)
<<<<<<< HEAD


<<<<<<< HEAD
@app.route('/jsonproducto')
def producto():
    conexionMySQL = mysql.connector.connect(
        host='10.9.120.5',
        user='kmill',
        passwd='kmill111',
        db='kmill'
    )
    sqlSelect = """SELECT * FROM Producto"""
    cursor = conexionMySQL.cursor()
    cursor.execute(sqlSelect)
    resultadoSQL = cursor.fetchone()
    cursor.close()
    conexionMySQL.close()
    return jsonify(resultadoSQL)

@app.route('/producto/<int:id>') 
def detalle_producto(id):
    conexionMySQL = mysql.connector.connect(
        host='10.9.120.5',
        user='kmill',
        passwd='kmill111',
        db='kmill'
    )
    sqlSelect = """SELECT Nombre, Descripción, Precio, stock FROM Producto WHERE id = %s"""
    cursor = conexionMySQL.cursor()
    cursor.execute(sqlSelect, (id,))
    resultadoSQL = cursor.fetchone()

    cursor.close()
    conexionMySQL.close()         
    return jsonify(resultadoSQL)

@app.route('/productoborrar/<int:id>', methods=['GET','DELETE']) 
def borrar_producto(id):
    conexionMySQL = mysql.connector.connect(
        host='10.9.120.5',
        user='kmill',
        passwd='kmill111',
        db='kmill'
    )
    sqlSelect = """ DELETE from Nombre, Descripción, Precio, stock FROM Producto WHERE id = %s"""
    cursor = conexionMySQL.cursor()
    cursor.execute(sqlSelect, (id,))
    resultadoSQL = cursor.fetchone()

    cursor.close()
    conexionMySQL.close()         
    return jsonify(resultadoSQL)


@app.route('/categoria/<int:id>') 
def detalle_categoria(id):
    conexionMySQL = mysql.connector.connect(
        host='10.9.120.5',
        user='kmill',
        passwd='kmill111',
        db='kmill'
    )
    sqlSelect = """SELECT Nombre FROM Categoria WHERE id = %s"""
    cursor = conexionMySQL.cursor()                                                        
    cursor.execute(sqlSelect, (id,))
    resultadoSQL = cursor.fetchone()

    cursor.close()
    conexionMySQL.close()
    return jsonify(resultadoSQL)

@app.route('/producto_ingrediente/<int:id>') 
def producto_ingrediente(id):
    conexionMySQL = mysql.connector.connect(
        host='10.9.120.5',
        user='kmill',
        passwd='kmill111',
        db='kmill'
    )
    #consulta 1
    qProducto = """SELECT Nombre FROM Producto WHERE id = %s"""
    cursor = conexionMySQL.cursor()
    cursor.execute(qProducto, (id,))
    product = cursor.fetchone()


   
   # SELECT i.Nombre from Ingrediente i 
    #INNER join Ingredientes_Productos ip ON i.id = ip.id_Ingredientes
    #INNER JOIN Producto p ON ip.id_Producto = p.id
    #WHERE ip.id_Ingredientes = 3
    #consulta 2
    qIngrediente = """ SELECT Nombre FROM Ingrediente WHERE id = %s """
    cursor.execute(qIngrediente, (id,))
    ingrediente = cursor.fetchall()
    
    cursor.close()

    resul = {  "nombre_pro": product[0],  # Nombre del producto
            "ingredientes":  [ingredient[0] for ingredient in ingrediente] }
    return jsonify(resul)

  #       "Producto": product,
  #"Ingredientes": ingrediente 

@app.route('/filtroproducto/') 
def filtro_producto():
   filtro = None

   if request.is_json:
     if filtro in request.json:
        filtro = request.json['filtro']

    
   conexionMySQL = mysql.connector.connect(
        host='10.9.120.5',
        user='kmill',
        passwd='kmill111',
        db='kmill'
    )
  
   if filtro == None:
    query = 'select * from Producto'
    cursor = conexionMySQL.cursor()
    result = cursor.execute(query,)
   elif filtro != None : 
    query = 'SELECT * FROM Producto where Nombre LIKE "%" || ? || "%"'
    cursor = conexionMySQL.cursor()
    result = cursor.execute(query, (filtro,))

    return result
  # arriba de mika 
=======
=======
>>>>>>> 90d04689c69db783a19ba251fe17d67e17931857
>>>>>>> c26567d1f95cbd2fa617dac76c6804ce00cb45b6
