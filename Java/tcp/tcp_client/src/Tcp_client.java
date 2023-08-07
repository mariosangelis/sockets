
import java.io.IOException;
import java.io.ObjectOutputStream;
import java.io.OutputStream;
import java.net.InetAddress;
import java.net.Socket;
import java.net.SocketException;

public class Tcp_client {

    public static void main(String[] args){
        
        Socket socket = null;
        int i=0;
        InetAddress server_address = null;
        byte[] buf=new byte[60000];

        try{
            server_address = InetAddress.getByName("192.168.1.101");
            socket = new Socket(server_address, 4448);
        } 
        catch (IOException ex) {
            System.out.println("IOException");
        }

        try{
            for(i=0;i<10;i++){
                student my_student=new student(i*1000,"marios angelis","Platonos 142");
            
                OutputStream outputStream = socket.getOutputStream();
                // create an object output stream from the output stream so we can send an object through it
                ObjectOutputStream objectOutputStream = new ObjectOutputStream(outputStream);

                System.out.println("Sending messages to the ServerSocket");
                objectOutputStream.writeObject(my_student);
            
            }
            socket.close();
        }
        catch(SocketException ex ){
            System.out.println("Socket Exception");
            System.exit(-1);
        } 
        catch (IOException ex) {
            System.out.println("IOException");
            System.exit(-1);
        }
    }
    
}
