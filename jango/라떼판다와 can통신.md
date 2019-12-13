# 라떼판다와 can통신



시리얼 통신으로 자동차로 한다 

usb  인식 ,시리얼 통신으로 할수있게 드라이버 설치

(명령부)

수신 id : 헥사코드로 이용한다. 

​				8진수로 표현 그데이터를 받는다 . 이걸 10진수로 바꾼다. 10진수를 2진수로 바꾼다 . 

​				다양한 커맨드를 보내고 받을수 있다 . 

(데이터)

​				id를 보내면서 데이터를 보낸다.  개보수적인 자동차 회사네 .....





APP = 시리얼 이 바쁘면 좀 있다 간다 .

리얼 타임으로 안온다 . 

시리얼 한테 시작과 끝을 알려주고 보낸다 

:U28 보내겠다 3F 체크섬 :암호화 같은것 김지훈 이 들어가면 6바이트 숫자마다 아스키코드 값을 모두 더해서 나누기 2를 해라 

체크섬 :규칙은 값다. 데이터가 정상인지 아닌지 구별 보내온 데이터와 받는 데이터가 같은지 확인 



자바에서 CAN통신 받기 . 

```java
package can;

import java.io.BufferedInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;

import gnu.io.CommPort;
import gnu.io.CommPortIdentifier;
import gnu.io.NoSuchPortException;
import gnu.io.SerialPort;
import gnu.io.SerialPortEvent;
import gnu.io.SerialPortEventListener;

public class SerialTest implements SerialPortEventListener {
	private SerialPort serialPort;
	private CommPortIdentifier portIdentifier;
	private CommPort commPort;
	private BufferedInputStream bin;
	private InputStream in;
	private OutputStream out;

	public SerialTest() {

	}

	public SerialTest(String portName) throws NoSuchPortException {
		portIdentifier = CommPortIdentifier.getPortIdentifier(portName);
		// 포트가 정상이면 CONNECT
		System.out.println("Connect Com Port!");
		try {
			connectSerial();
			System.out.println("Connect OK !!");
			(new Thread(new SerialWriter())).start(); //
		} catch (Exception e) {
			System.out.println("Connect Fail !!");
			e.printStackTrace();
		}
	}
	
	
	private class SerialWriter implements Runnable {
		String data;

		public SerialWriter() {
			this.data = ":G11A9\r"; //나도 같이 참가 하겠습니다 .
		}

		public SerialWriter(String serialData) {
			// W28 00000000 000000000000
			// :W28 00000000 000000000000 53 \r
			String sdata = sendDataFormat(serialData);
			System.out.println(sdata);
			this.data = sdata;
		}
		
		public String sendDataFormat(String serialData) {
			serialData = serialData.toUpperCase();
			char c[] = serialData.toCharArray();
			int cdata = 0;
			for (char cc : c) {
				cdata += cc;
			}
			cdata = (cdata & 0xFF);

			String returnData = ":";
			returnData += serialData + Integer.toHexString(cdata).toUpperCase();
			returnData += "\r";
			return returnData;
		}

		public void run() {
			try {

				byte[] inputData = data.getBytes();

				out.write(inputData);
			} catch (Exception e) {
				e.printStackTrace();
			}
		}

	}
	

		

	
	
	
	
	

	public void connectSerial() throws Exception {

		if (portIdentifier.isCurrentlyOwned()) {
			System.out.println("Error: Port is currently in use"); //그래도문제가 있으면 하지마라, 다른 사람이 쓰고 있다. 
		} else {
			commPort = portIdentifier.open(this.getClass().getName(), 5000);
			if (commPort instanceof SerialPort) { 
				serialPort = (SerialPort) commPort; //COMMPORT 
				serialPort.addEventListener(this); //
				serialPort.notifyOnDataAvailable(true);
				serialPort.setSerialPortParams(921600, // 통신속도 
						SerialPort.DATABITS_8, // 데이터 비트
						SerialPort.STOPBITS_1, // stop 비트
						SerialPort.PARITY_NONE); // 패리티 우리가 전송하는건 검증 하겠다 .
				in = serialPort.getInputStream();
				bin = new BufferedInputStream(in);
				out = serialPort.getOutputStream();
			} else {
				System.out.println("Error: Only serial ports are handled by this example.");
			}
		}
	}

	public static void main(String[] args) {
		try {
			new SerialTest("COM5"); //CAN 버스 시리얼 포트 넘버를 입력한다. 
		} catch (NoSuchPortException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}

	@Override
	public void serialEvent(SerialPortEvent event) {
		switch (event.getEventType()) {
		case SerialPortEvent.BI:
		case SerialPortEvent.OE:
		case SerialPortEvent.FE:
		case SerialPortEvent.PE:
		case SerialPortEvent.CD:
		case SerialPortEvent.CTS:
		case SerialPortEvent.DSR:
		case SerialPortEvent.RI:
		case SerialPortEvent.OUTPUT_BUFFER_EMPTY:
			break;
		case SerialPortEvent.DATA_AVAILABLE:
			byte[] readBuffer = new byte[128]; 

			try {

				while (bin.available() > 0) {
					int numBytes = bin.read(readBuffer);
				}

				String ss = new String(readBuffer);
				System.out.println("Receive Low Data:" + ss + "||");

			} catch (Exception e) {
				e.printStackTrace();
			}
			break;
		}
	}


}

```





## 안드로이드와  CAN  BUS  연결

PAD 제공 





























