Markdown 사용 테스트
: 큰 제목

==============

작은 제목

--------------------

# 제목 1

## 제목 2

### 제목 3

#### 제목 4

##### 제목 5

###### 제목 6

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
--------------

2022/06/21(화) 누리호 발사 성공

```js
	import React from 'react';
function MyComponent(props) {
	if (props.isBar) {
		return <div>Bar< / div>;
	}
	return <div>Foo< / div>;
}
export default MyComponent;
```

누리호 성공 축하!!!!

------------------------------------------

2022/06/21(화) 누리호 발사 성공

	세계에서 7번째 우주 강국

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

각각  태그로 변환됨

문장 중간에 사용할 경우 띄어쓰기를 하는 것이 좋음

// examle
	
이텔릭체 *별표(asterisks)* 혹은 _언더바(underscore)_ 를 사용

두껍게는 **별표(asterisks)* 혹은 __언더바(underscore)__를 사용

**_이텔릭체_와 두껍게**를 같이 사용할 수 있음

취소선은 ~~물결표시(tilde)~~를 사용

----------------------------------------------------

1. Images

* 영상을 화면에 출력, ‘!’, ‘[ ]‘ 그리고 ‘( )'를 이용

* 영상이 웹 사이트에 같이 있어야 함

* 혹은 경로 지정해서 영상 사용

![alt text](image url "image Title")

// examle 1
	
![Street](TestImage.jpg "Oxford")

// examle 2
	
Inline-style:
	
![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")

Reference-style:
![alt text][logo]

[logo]: https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 2"

* 크기조절

// example 3

<img src="TestImage.jpg" width="450px" height="300px" title="px(픽셀) 크기 설정" alt="RubberDuck"></img><br/>
<img src="TestImage.jpg" width="40%" height="30%" title="px(픽셀) 크기 설정" alt="RubberDuck"></img>


2. Footnotes

* 각주는 핵심 Markdown 사양의 일부가 아니지만 GFM에서 지원

* '^'기호 사용

Here is a simple footnote[^1].

A footnote can also have multiple lines[^2].

You can also use words, to fit your writing style more closely[^note].

[^1]: My reference.
[^2]: Every new line should be prefixed with 2 spaces.
This allows you to have a footnote with multiple lines.
[^note]:
Named footnotes will still render with numbers instead of the text but allow easier identification and linking.
This footnote also has been made with a different syntax using 4 spaces for new lines.


3. Table

* <table> 태그로 변환됨

* 헤더 셀을 구분할 때 3개 이상의 -(hyphen/dash) 기호가 필요함

* 헤더 셀을 구분하면서 :(Colons) 기호로 셀(열/칸) 안에 내용을 정렬할 수 있음

* 가장 좌측과 가장 우측에 있는 ‘|(vertical bar)” 기호는 생략 가능

// example 1

| 값 | 의미 | 기본값 |
|---|:---:|---:|
| `static` | 유형(기준) 없음 / 배치 불가능 | `static` |
| `relative` | 요소 자신을 기준으로 배치 | |
| `absolute` | 위치 상 부모(조상)요소를 기준으로 배치 | |
| `fixed` | 브라우저 창을 기준으로 배치 | |

// example 2

Markdown | Less | Pretty
--- | --- | ---
*Still* | `renders` | **nicely**
1 | 2 | 3


4. 줄 바꿈

* 일반 텍스트 문장: 문장 끝에 공백 2번(스페이스 2번)하면 줄 바꿈이 됨.

* 테이블 내에서나 일반적인 경우: '<br>' 사용

// example 1

예를 들어, 지금
공백 2번 만들어서 지금과 공백 사이에서 줄 바꿈이 된다.

// example 2

안녕하세요. <br>반갑습니다. 줄이 바뀌었어요.


