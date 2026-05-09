# 과제 2. Queue 기반 작업 분배

## 목표
1개 producer, 3개 worker, 100개 작업.

## 요구사항
- producer 가 0~99를 queue에 put
- worker 3개가 동시에 get → 처리(예: x*x)
- 모든 작업 완료 후 worker 종료
- 결과 합계 출력
