
import java.net.*;
import java.io.*;

public class EjServer_msg {

    public static void main(String[] args) {

        // Declaracion del socket Servidor
        ServerSocket so_serv;

        //Declaracion del OutStream donde escribira el Socket de la conexion
        PrintStream data_out_conex;

        try { // try 1
            //crea el socket Server atendiendo en el puerto 7000
            so_serv = new ServerSocket(7000);
            System.out.println("Servidor atendiendo en el puerto 7000");
            try {
                while (true) {

                    // crea el PrintStream con el OutputStream del socket
                    try ( // Declara un socket para atender la conexion
                            Socket so_conex = so_serv.accept()) {
                        // crea el PrintStream con el OutputStream del socket
                        data_out_conex = new PrintStream(so_conex.getOutputStream());
                        data_out_conex.println("Se a conectado al socket servidor ");
                    }
                } //fin del while
            } // end try
            catch (UnknownHostException e) {
                // si hubo error lo envia a la salida por defecto
                System.out.println(e);
            } // end catch
            catch (IOException e) {
                // si hubo error lo envia a la salida por defecto
                System.out.println(e);
            }
            //cierra el socket Server
            so_serv.close();
        } // Cierra try 1
        catch (IOException e) {
            // si hubo error lo envia a la salida por defecto
            System.out.println(e);
        }
    }
}

/*
El programa que proporcionaste es un servidor que escucha en el puerto 7000 y envía un mensaje al cliente cuando este se conecta. 
El servidor está configurado para manejar múltiples conexiones de clientes de forma secuencial.

En este servidor, se utiliza un bucle infinito para escuchar y aceptar conexiones entrantes en el puerto 7000. 
Cuando un cliente se conecta, se crea un nuevo socket para manejar la comunicación con ese cliente en particular. 
El servidor envía un mensaje al cliente y luego cierra la conexión.

Este tipo de servidor es útil para realizar pruebas simples de conexiones cliente-servidor, 
pero no es adecuado para aplicaciones que requieren una comunicación bidireccional continua o un manejo más sofisticado de múltiples clientes.

Puedes compilar y ejecutar este servidor para que escuche en el puerto 7000 y acepte conexiones entrantes. 
Asegúrate de que el cliente se conecte al puerto 7000 para recibir el mensaje "Se ha conectado al socket servidor".
*/
