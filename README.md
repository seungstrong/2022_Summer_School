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


Code Block Method 1  "<pre><code> {code} </code></pre>"이용방법
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


1.각 기호를 3개 이상 사용
마크다운 문서를 미리 보기로 출력할 때 페이지 나누기 용도로 많이 사용
사용 기호
* * *
***
*****
- - -
--------------------------
* * *
ㅇㅅㅇ
***
ㅇㅅㅇ
*****
ㅇㅅㅇ
- - -
ㅇㅅㅇ
---------------

* 참조 링크

[link keyword][id]

[id]: URL "Optional Title here"

// examle
Link: [google][googlelink]

Naver:[naver][naversite]

[googlelink]: https://google.co.uk "Let's Go Google"

[naversite]:https://www.naver.com "Let's go naver"


* 외부 링크

[Title](link)

// examle

[Google](https://google.co.uk "Let's Go Google“)


* 자동 링크

 문서 내 일반 URL이나 꺽쇠 괄호(‘< >’) 안의 URL은 자동으로 연결

 일반적인 URL 혹은 이메일 주소인 경우

// examle

Google Homepage: https://google.co.uk

Naver Homepage: <https://naver.com>

-----------------------------------------------
* 강조하기(Emphasis)

텍스트를 강조할 때 사용하는 문법

각각 <em>, <strong>, <del> 태그로 변환됨

문장 중간에 사용할 경우 띄어쓰기를 하는 것이 좋음

// examle
이텔릭체 *별표(asterisks)* 혹은 _언더바(underscore)_를 사용

두껍게는 ** 별표(asterisks)* 혹은 __언더바(underscore)__를 사용

**_이텔릭체_와 두껍게**를 같이 사용할 수 있음

취소선은 ~~물결표시(tilde)~~를 사용