
/**
 * @author camilo
 *
 * Ejercicio 4
 * Realizar el ejemplo anterior, utilice una maquina Linux del laboratorio para probar el programa.
 */
import java.net.*;
import java.io.*;

public class Echo {

    public static void main(String[] args) {
        // Declaración del socket
        Socket so_echo;
        // Declaración del InputStream para el socket
        DataInputStream data_in_socket;
        // Declaración del InputStream para la línea de comandos
        DataInputStream data_in_consola;
        String linea;
        // Declaración del OutputStream
        PrintStream data_out_socket;
        // Declaración del nombre del host servidor echo
        String host = "localhost"; // Puedes cambiar esto a la dirección del servidor echo que desees

        try {
            // Crea el socket y se intenta conectar al servidor echo en el puerto 7
            so_echo = new Socket(host, 7);

            // Crea el DataInputStream con InputStream del socket
            data_in_socket = new DataInputStream(so_echo.getInputStream());
            // Crea el PrintStream con el OutputStream del socket
            data_out_socket = new PrintStream(so_echo.getOutputStream());

            // Crea el DataInputStream para la entrada de la consola
            data_in_consola = new DataInputStream(System.in);

            while (true) {
                // Lee una línea desde la consola
                linea = data_in_consola.readLine();
                if (linea.equals(".")) {
                    break;
                }
                // Envía la línea al Stream del Socket
                data_out_socket.println(linea);
                // Lee los datos del InputStream del socket y los envía a la salida estándar
                System.out.println(data_in_socket.readLine());
            } // fin del while

            // Cierra la conexión
            so_echo.close();
        } // end try
        catch (UnknownHostException e) {
            // Si hubo error, lo envía a la salida por defecto
            System.out.println(e);
        } // end catch
        catch (IOException e) {
            // Si hubo error, lo envía a la salida por defecto
            System.out.println(e);
        }
    }
}
