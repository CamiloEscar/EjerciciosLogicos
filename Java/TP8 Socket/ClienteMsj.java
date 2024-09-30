
/**
 * @author camilo
 *
 * Ejercicio 6
 * Realizar un programa cliente que se conecte al servidor del ejemplo anterior, lea los datos que le envía el
 * servidor y los envíe a la salida estándar de SO (el programa recibe los datos de nombre de host y puerto al
 * que debe conectarse desde línea de comandos) . Para verificar el funcionamiento debe dejar el programa
 * del servidor corriendo en algún host de un compañero y corra este programa en otro host.
 * Ej. En la maquina servidor nombre_server#java Server_msg 3500
 * En la maquina cliente nombre_cliente#java Cliente_msg nombre_server 3500
 */
import java.net.*;
import java.io.*;

public class ClienteMsj {

    public static void main(String[] args) {
        if (args.length != 2) {
            System.out.println("Uso: java Cliente_msg <nombre_del_host> <puerto>");
            return;
        }

        String host = args[0];
        int port = Integer.parseInt(args[1]);

        try {
            Socket socket = new Socket(host, port);
            DataInputStream inputStream = new DataInputStream(socket.getInputStream());

            while (true) {
                String serverData = inputStream.readLine();
                if (serverData == null) {
                    break;
                }
                System.out.println(serverData);
            }

            socket.close();
        } catch (UnknownHostException e) {
            System.err.println("Error: Nombre de host desconocido - " + e.getMessage());
        } catch (IOException e) {
            System.err.println("Error de E/S - " + e.getMessage());
        }
    }
}

//Para ejecutar el cliente, utiliza el siguiente comando en la máquina cliente:
//java Cliente_msg <nombre_del_host> <puerto>
