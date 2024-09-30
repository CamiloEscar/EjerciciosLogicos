
/**
 * @author camilo
 *
 * Ejercicio 5
 * Modifique el programa anterior para que el servidor atienda en el puerto que recibe desde línea de comando
 * por ej. Linux_machine> java Server_msg 7000.
 */
import java.net.*;
import java.io.*;

public class ServerMsg {

    public static void main(String[] args) {
        if (args.length != 1) {
            System.out.println("Uso: java Server_msg <puerto>");
            return;
        }

        int port = Integer.parseInt(args[0]);

        ServerSocket so_serv;
        PrintStream data_out_conex;

        try {
            so_serv = new ServerSocket(port);
            System.out.println("Servidor atendiendo en el puerto " + port);

            try {
                while (true) {
                    try (Socket so_conex = so_serv.accept()) {
                        data_out_conex = new PrintStream(so_conex.getOutputStream());
                        data_out_conex.println("Se ha conectado al socket servidor");
                    }
                }
            } catch (UnknownHostException e) {
                System.out.println(e);
            } catch (IOException e) {
                System.out.println(e);
            }

            so_serv.close();
        } catch (IOException e) {
            System.out.println(e);
        }
    }
}

// Para compilar y ejecutar el programa con un puerto específico, puedes usar el siguiente comando:
// java Server_msg 7000

