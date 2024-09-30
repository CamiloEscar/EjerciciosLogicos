
/**
 * @author camilo
 *
 * Ejercicio 1
 * Realizar un programa que permita determinar a cuales de los puertos entre el 1 al 1024 se puede establecer
 * una conexi�n a : 1) - al host local 2) una maquina Linux del laboratorio.
 *
 * Para realizar un programa en Java que permita determinar a qu� puertos del rango del 1 al 1024
 * se puede establecer una conexi�n, tanto al host local como a una m�quina Linux en el laboratorio, necesitar�s usar sockets.
 * Debes crear dos versiones del programa, una para probar la conexi�n al host local y otra para la m�quina Linux.
 */

public class CheckPorts {

    public static void main(String[] args) {
        String hostLocal = "localhost"; // Puedes usar "127.0.0.1" en lugar de "localhost"
        String hostLinux; // Reemplaza con la direcci�n IP de la m�quina Linux
        hostLinux = "IP de linux";

        // Define el rango de puertos a verificar
        int startPort = 1;
        int endPort = 1024;

        // Verifica la conexi�n en el host local
        System.out.println("Comprobando conexiones al host local:");
        checkPorts(hostLocal, startPort, endPort);

        // Verifica la conexi�n en la m�quina Linux
        System.out.println("\nComprobando conexiones a la m�quina Linux:");
        checkPorts(hostLinux, startPort, endPort);
    }

    private static void checkPorts(String host, int startPort, int endPort) {
        for (int port = startPort; port <= endPort; port++) {
            try {
                System.out.println("Puerto " + port + " abierto");

            } catch (Exception e) {
                // No se pudo establecer la conexi�n, el puerto est� cerrado o protegido.
            }
        }
    }
}
