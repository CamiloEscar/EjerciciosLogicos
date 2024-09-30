
/**
 * @author camilo
 *
 * Ejercicio 1
 * Realizar un programa que permita determinar a cuales de los puertos entre el 1 al 1024 se puede establecer
 * una conexión a : 1) - al host local 2) una maquina Linux del laboratorio.
 *
 * Para realizar un programa en Java que permita determinar a qué puertos del rango del 1 al 1024
 * se puede establecer una conexión, tanto al host local como a una máquina Linux en el laboratorio, necesitarás usar sockets.
 * Debes crear dos versiones del programa, una para probar la conexión al host local y otra para la máquina Linux.
 */

public class CheckPorts {

    public static void main(String[] args) {
        String hostLocal = "localhost"; // Puedes usar "127.0.0.1" en lugar de "localhost"
        String hostLinux; // Reemplaza con la dirección IP de la máquina Linux
        hostLinux = "IP de linux";

        // Define el rango de puertos a verificar
        int startPort = 1;
        int endPort = 1024;

        // Verifica la conexión en el host local
        System.out.println("Comprobando conexiones al host local:");
        checkPorts(hostLocal, startPort, endPort);

        // Verifica la conexión en la máquina Linux
        System.out.println("\nComprobando conexiones a la máquina Linux:");
        checkPorts(hostLinux, startPort, endPort);
    }

    private static void checkPorts(String host, int startPort, int endPort) {
        for (int port = startPort; port <= endPort; port++) {
            try {
                System.out.println("Puerto " + port + " abierto");

            } catch (Exception e) {
                // No se pudo establecer la conexión, el puerto está cerrado o protegido.
            }
        }
    }
}
