
import java.net.*;
import java.io.*;

public class EjDaytime {

    public static void main(String[] args) {

        Socket so_daytime; // declaracion del socket
        DataInputStream data_daytime; // declaracion del DataInputStream
        String host = "www.ora.com";
        //String host = "10.10.11.2"; // al server del lab

        try {
            //crea el socket y se intenta conectar
            so_daytime = new Socket(host, 13);
            // crea el DataStream con InputStream del socket
            data_daytime = new DataInputStream(so_daytime.getInputStream());

            //lee una linea en el Stream,
            //en el stream estan los datos enviados por el server
            String line = data_daytime.readLine();

            // verifica el nombre del host y el puerto donde se conecto
            System.out.println("conectado a :" + so_daytime.getInetAddress());
            System.out.println("port :" + so_daytime.getPort());
            System.out.println("dia y hora :" + line);
            so_daytime.close();
        } // end try
        catch (UnknownHostException e) {
            // si hubo error lo envia a la salida por defecto
            System.out.println(e);
        } // end catch
        catch (IOException e) {
            // si hubo error lo envia a la salida por defecto
            System.out.println(e);
        }
    }
}

/*
1-2. Importas las clases necesarias del paquete java.net y java.io.

Comienzas la declaración de la clase Daytime.

Inicias el método main, que es el punto de entrada de la aplicación.

Declaras una variable so_daytime para representar el socket que se utilizará para la conexión al servidor daytime.

Declaras una variable data_daytime que será un DataInputStream utilizado para leer datos del socket.

Especificas el host al que te quieres conectar. En este caso, "www.ora.com" es el host de ejemplo. Puedes cambiarlo si deseas.

Puedes comentar la línea 10 y descomentar la línea 11 si deseas conectarte a un servidor en el laboratorio con una dirección IP local.

13-37. Comienzas un bloque try para manejar las excepciones que pueden ocurrir al intentar establecer la conexión y leer datos del servidor.

Intentas crear un nuevo objeto de tipo Socket para conectar al host especificado en el puerto 13, que es el puerto estándar del protocolo "daytime".

Creas un DataInputStream llamado data_daytime utilizando el InputStream del socket para poder leer datos.

Lees una línea desde el DataInputStream. En el protocolo "daytime", el servidor responde con la fecha y hora actuales.

24-25. Verificas e imprimes la dirección del host al que te has conectado y el puerto al que te has conectado.

Imprimes la línea que contiene la fecha y hora recibida del servidor.

Cierras la conexión al servidor.

30-33. Capturas la excepción UnknownHostException, que se lanza si no se puede resolver el nombre de host, e imprimes el error.

34-37. Capturas la excepción IOException, que se lanza si ocurre algún error de E/S durante la conexión o lectura, e imprimes el error.

Este programa se conecta al servidor daytime en el host especificado y muestra la fecha y hora que recibe del servidor. Ten en cuenta que 
este es un ejemplo simple de conexión TCP y que, en una aplicación real, se pueden realizar más operaciones y manejar excepciones de manera más detallada.
*/
