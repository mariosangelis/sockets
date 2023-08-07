
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.SocketException;
import java.net.UnknownHostException;

public class Udp_client {

    public static void main(String[] args){
        
        DatagramSocket socket = null;
        InetAddress server_address = null;
        byte[] buf=new byte[60000];

        try{
            socket = new DatagramSocket();
            server_address = InetAddress.getByName("192.168.1.101");
        }
        catch (UnknownHostException ex) {
            System.out.println("Unknown Host Exception");
            System.exit(-1);
        }
        catch (SocketException ex) {
            System.out.println("Socket Exception");
            System.exit(-1);
        }
        
        student my_student=new student(10,"marios angelis","Platonos 142");
        
        try{
            ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
            ObjectOutputStream os = new ObjectOutputStream(outputStream);
            os.writeObject(my_student);
            byte[] data = outputStream.toByteArray();

            DatagramPacket packet  = new DatagramPacket(data, data.length, server_address, 4448);
            System.out.println("Send a message to server");
            socket.send(packet);

            packet = new DatagramPacket(buf, buf.length);
            socket.receive(packet);
            String received = new String(packet.getData(), 0, packet.getLength());
            System.out.println("Received message = "+received+" message length="+received.length());
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
