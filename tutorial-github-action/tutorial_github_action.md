
# Github Action

## Github Action 개념

- **Automates development workflow** (as much as possible)
	- 워크플로우는 다음을 포함할 수 있음
		- merge code ...
		- test
		- build
		- deploy
		- etc 
- Github Action은 레포지토리에서 발생, 추가되는 모든 이벤트에 대해 상응하는 어떠한 액션을 자동으로 취할 수 있게 하는 유용한 기술
	- Listen to event
	- Tribber Workflow
- Github Action은 Github 플랫폼과 일체형으로 매우 편리하고 안정적임

## Workflow 예시 : CI/CD Pipeline

- 기본적인 CI/CD 프로세스
	- `commit code -> test -> build -> push -> deploy`
		- 필요한 구성요소들 설치, 설정, 플러그인 연결 등 해야할 일들이 너무 많이 생김
- Git	hub Action은 이러한 구성요소를 갖추는 과정을 일원화 할 수 있음
	- Github Action은 필요한 요소들이 조합된 환경을 제공함
	- Github Action workflow template은 YAML 포맷으로 되어 있으며, 취하고자 하는 액션을 정의할 수 있음
		- 미리 제공되어 있는 템플릿을 사용하면 편함

## Workflow template

```yaml
name:
on:
	[event1]:
		branches:
	[event2]:
		branches

jobs:
	build:
		
```

- name
- on
	- branches
- jobs
	- build
		- runs-on
		- steps
			- uses
			- with
			- run

## Github Events & Actions



## CI/CD Pipeline



## Reference

[TechWorld with Nana - Github Action Tutorial](https://youtu.be/R8_veQiYBjI)