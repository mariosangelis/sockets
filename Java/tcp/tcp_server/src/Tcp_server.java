
import java.io.IOException;
import java.io.InputStream;
import java.io.ObjectInputStream;
import java.net.ServerSocket;
import java.net.Socket;
import java.net.SocketException;

public class Tcp_server {
    
    public static void main(String[] args){
        
        ServerSocket serverSocket = null;
        Socket  clientSocket = null;
        
        try {
            serverSocket=new ServerSocket(4448);
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
}
