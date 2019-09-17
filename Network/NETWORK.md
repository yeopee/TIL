# NETWORK



프로세스: 실행중인 프로그램(exe,브라우저)

쓰레드 : 포로세스 안에서 실행되는것 

메모리를 적게 사용한다. 

서버에 쓰레드를 잘 쓴다.

멀티태스킹:여러가지 프로세스를 작업한다, 

멀티쓰레딩:프로세스안에 여러가지쓰레드가 돈다. 

일반적인 프로세스 

```java
package day01;

public abstract class T1 {

	public static void main(String[] args) throws InterruptedException {
		for(int i=0;i<20;i++) {
			Thread.sleep(10);
			System.out.println("A:"+i);
		}
		System.out.println("end");
		for(int i=0;i<20;i++) {
			Thread.sleep(10);
			System.out.println("B:"+i);
		}
		
	}
	
	

}

```

웹페이지도 쓰레드를 통해 다른 작업 가능하다 .

쓰레드의 우선 순위 를 설정할수 있다. 

```java
public class Th1 {

	public static void main(String[] args) {
		MyThread t1 = new MyThread("T1");
		MyThread t2 = new MyThread("T2");
		MyThread t3 = new MyThread("T3");
		t1.setPriority(1);
		t2.setPriority(2);
		t3.setPriority(10);

		t1.start();
		t2.start();
		t3.start();

	}

}
```

```java
package day01;

class MyThread extends Thread{
	String name;
	public MyThread(String name){
		this.name=name;
	}
	
	@Override
	public void run() {
	for(int i =0;i<1000;i++) {
		try {
			Thread.sleep(3);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		yield(); //t3가 계속 도는거 방지 (양보) 
		System.out.println(name+":"+i);
		}	
	
	}
	
}



public class Th1 {

	public static void main(String[] args) {
		MyThread t1 = new MyThread("T1");
		MyThread t2 = new MyThread("T2");
		MyThread t3 = new MyThread("T3");
		t1.setPriority(1);
		t2.setPriority(2);
		t3.setPriority(10);

		t1.start();
		t2.start();
		t3.start();

	}

}

```

yield() : 양보 쓰레드 하나가 계속 도는걸 방지 

while 죽이는 코드

```java
package day01;

class SaveThread extends Thread{
	public void run() {
		while(true) {
			try {
				Thread.sleep(2000);
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			save();
		}
	}
	public void save(){
		System.out.println("SAVE...");

	}
}


public class Th4 {

	public static void main(String[] args) {
			SaveThread st =new SaveThread();
			st.setDaemon(true);//무한루프가 종료가된다. 
			st.start();
			for(int i=0;i<20;i++) {
				try {
					Thread.sleep(500);
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				System.out.println(i);
			}
	}

}

```











WS : Scanner 를 받아서 그 숫자만큼 출력 

```java
package day01;

import java.util.Scanner;

class Exth extends Thread{
	public void run() {
		while(true) {
			try {
				Thread.sleep(2000);
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
	}
}



public class Th5 {

	public static void main(String[] args) {
		Exth et = new Exth();
		et.setDaemon(true);
		et.start();
		System.out.println("input num");
		Scanner sc =new Scanner(System.in);
		int num = sc.nextInt();
		for(int i=0;i<num;i++) {
			try {
				Thread.sleep(500);
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			System.out.println(i);
		}
	}

}


```

