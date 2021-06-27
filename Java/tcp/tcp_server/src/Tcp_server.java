
import java.io.IOException;
import java.io.InputStream;
import java.io.ObjectInputStream;
import java.net.InetAddress;
import java.net.NetworkInterface;
import java.net.ServerSocket;
import java.net.Socket;
import java.net.SocketException;
import java.util.Enumeration;

public class Tcp_server {
    
    public static InetAddress server_address;
    
    public static void main(String[] args){
        
        ServerSocket serverSocket = null;
        Socket  clientSocket = null;
        set_ip_address();
        
        
        try {
            serverSocket=new ServerSocket(4448,1,server_address);
        } 
        catch (IOException ex) {
            System.out.println("IOException");
        } 

        while(true){
            
            try{
                System.out.println("Waiting for connections");
                clientSocket = serverSocket.accept();
                System.out.println("Accepted a connection");
                
                while(true){
                    
                    InputStream inputStream = clientSocket.getInputStream();
                    // create a DataInputStream so we can read data from it.
                    ObjectInputStream objectInputStream = new ObjectInputStream(inputStream);
                    // read the list of messages from the socket
                    student my_student = (student) objectInputStream.readObject();          
                    System.out.println("Received "+my_student);
                    
                }
            }
            catch(SocketException ex ){
                System.out.println("Socket Exception");
                System.exit(-1);
            }
            catch (IOException ex) {
                System.out.println("Connection closed");
                System.exit(1);
            } 
            catch (ClassNotFoundException ex) {
                System.out.println("Class Not Found Exception");
            }
        }   
    }    
    
    private static void set_ip_address(){
        
        Enumeration network_interfaces_list = null;
        try {
            network_interfaces_list = NetworkInterface.getNetworkInterfaces();

            while(network_interfaces_list.hasMoreElements()){
                NetworkInterface current_interface = (NetworkInterface) network_interfaces_list.nextElement();
                        
                Enumeration inet_addresses_list = current_interface.getInetAddresses();
                while (inet_addresses_list.hasMoreElements()){
                    
                    InetAddress current_inet_address = (InetAddress) inet_addresses_list.nextElement();
                    if(current_inet_address.getHostAddress().contains("127.")){break;}
                    
                    server_address=current_inet_address;       
                }
            }
        }
        catch (SocketException ex) {
            System.out.println("Socket exception inside set_ip_address method");
            System.exit(-1);
        }
    }
}
