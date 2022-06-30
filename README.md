Department : Andong National University (ANU), Computer Science Department
==========
1. Summer School(Engineering Communication)
-----------------
# 1.1 
## 2.1
### 3.1
#### 4.1
##### 5.1
######

인용문자 사용해보기
>This is a first blockqute.
>	>	This is a second blockqute.
>	>	>This is a third blockqute.

순서가 있는목록 - 숫자, 점을 사용
1. 첫번째
	-첫번째
2. 두번째
	-두번째
3. 세번째
	-세번째

순서가 없는 목록(글머리 기호 사용: *, +, - 사용)
* Blue
	* Green
		* Red
+ Blue
	+ Green
		+ Red
- Blue
	- Green
		- Red

순서가 없는 목록(혼합 사용)
* 1st Stage
	- 2nd Stage
		+ 3rd Stage
			+ 4th Stage


들여쓰기
-------------

2022/06/21(화) 누리호 발사 성공

	class Pizza {
	public:
		Pizza(int s) :size(s) {}
		int size;
	};

	void makeDouble(Pizza &p)
	{
		p.size *= 2;
	}

	int main()
	{
	
		return 0;
	}

누리호 성공 축하!!!!


한 줄 띄우지 않으면 줄바꿈인식 제대로 안됨 예시
----------------------------------------------------
2022/06/21(화) 누리호 발사 성공
	세계에서 7번째 우주 강국
누리호 성공 축하!!!!


Code Block Method 1  <!--<pre><code> {code} </code></pre>-->이용방법
------------------------------------------------------------------------------
<pre>
<code>
	class Car {
		private String modelName;
		private int modelYear;
		private String color;
		private int maxSpeed;
		private int currentSpeed;
		Car(String modelName, int modelYear, String color, int maxSpeed) {
			this.modelName = modelName;
			this.modelYear = modelYear;
			this.color = color;
			this.maxSpeed = maxSpeed;
			this.currentSpeed = 0;
		}
	}
</code>
</pre>


Code Block Method 2  “ ‘ ‘ ‘ “ 이용방법
--------------------------------------------
```
import React from 'react';
function MyComponent(props) {
if (props.isBar) {
return <div>Bar</div>;
}
return <div>Foo</div>;
}
export default MyComponent;
```


#Code Block Method 3
##코드블럭 시작점(" ''' ")에 사용하는 언어를 선언하여 문법 강조 가능
---------------------------------------------------------------------------
``` js
import React from 'react';
function MyComponent(props) {
if (props.isBar) {
return <div>Bar</div>;
}
return <div>Foo</div>;
}
export default MyComponent;
```