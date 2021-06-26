
import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.SocketException;
import java.net.UnknownHostException;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;

public class Udp_server {
    
    public static void main(String[] args){
        
        Charset charset = StandardCharsets.US_ASCII;
        DatagramSocket socket = null;
        InetAddress server_address = null;

        byte[] buf=new byte[60000];
        
        try {
            server_address = InetAddress.getByName("127.0.0.1");
            socket = new DatagramSocket(4448,server_address);
        } 
        catch (UnknownHostException ex) {
            System.out.println("Unknown Host Exception");
            System.exit(-1);
        }
        catch (SocketException ex) {
            System.out.println("Socket Exception");
            System.exit(-1);
        }
        
        
        while(true){
            
            try{
                DatagramPacket incomingPacket = new DatagramPacket(buf, buf.length);
                System.out.println("Wait to receive a message");
                socket.receive(incomingPacket);


                ByteArrayInputStream in = new ByteArrayInputStream(incomingPacket.getData());
                ObjectInputStream is = new ObjectInputStream(in);
                try {
                    student received_student = (student) is.readObject();
                    System.out.println("Student object received = "+received_student);
                } 
                catch (ClassNotFoundException e) {
                    System.out.println("Class Not Found Exception");
                    System.exit(-1);
                }

                InetAddress client_address = incomingPacket.getAddress();
                int client_port = incomingPacket.getPort();

                System.out.println("Packet length="+incomingPacket.getLength());
                String reply_message = "ACK";
                byte[] byteArrray = charset.encode(reply_message).array();

                DatagramPacket packet = new DatagramPacket(byteArrray, byteArrray.length, client_address, client_port);
                socket.send(packet);
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
}
