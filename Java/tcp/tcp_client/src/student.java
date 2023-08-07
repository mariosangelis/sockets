import java.io.Serializable;

    public class student implements Serializable {

        public student(int length, String name, String address1) {
            this.id = id;
            this.name = name;
            this.addressLine = address1;
            this.buf=new byte[length];
        }

        private static final long serialVersionUID = 1L;
        private int id;
        private String name;
        private String addressLine;
        private byte [] buf=null;

        public int getId() {
            return id;
        }

        public void setId(int id) {
            this.id = id;
        }

        public String getName() {
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }

        public String getAddressLine() {
            return addressLine;
        }

        public void setAddressLine(String addressLine) {
            this.addressLine = addressLine;
        }
        
        public int getBufferLength(){
            return this.buf.length;
        }

        public String toString() {
            return "Id = " + getId() + " Name = " + getName() + " Address = " + getAddressLine() + " buffer length = "+getBufferLength();
        }
}
