import time

class Process:
    def __init__(self, name, burstTime): # 프로세스는 이름과 버스트타임을 가집니다
        self.name = name
        self.burstTime = burstTime
        self.state = "준비" # 준비로 초기화

    # 프로세스 실행
    def execute(self, quantum):
        print(f"{self.name} 실행중...")

        if self.burstTime <= quantum:
            time.sleep(self.burstTime)
            self.state = "완료"

            print(f"프로세스 {self.name}가 완료로 바뀝니다.")

        else:
            time.sleep(quantum)
            self.burstTime -= quantum

            print(f"프로세스 {self.name}가 {quantum}초만큼 실행되었습니다.")

class RoundRobin:
    def __init__(self, processes, quantum): # 프로세스 리스트와 퀀텀을 가집니다
        self.processes = processes
        self.quantum = quantum

    def run(self):
        # 프로세스 리스트가 전부 완료가 아니면 True
        while any(process.state != "완료" for process in self.processes):
            
            #프로세스 리스트 for루프
            for process in self.processes:
                
                # 준비 상태이면 실행시켜줍니다
                if process.state == "준비":
                    process.state == "실행"
                    process.execute(self.quantum)

                    # 버스트타임이 0이 됐으면 완료상태로 전환
                    if process.burstTime <= 0:
                        process.state = "완료"

                # 이미 완료 상태이면 컨티뉴
                elif process.state == "완료":
                    continue

            # 전체 프로세스 상태 출력     
            print("\n   | 프로세스 |  상태  |")
            for process in self.processes:
                print(f'\t{process.name}\t {process.state}')
            print("")

if __name__ == "__main__":
    # 시간 측정 시작
    start = time.perf_counter()
    
    # 프로세스 생성
    p1 = Process("P1", 10)
    p2 = Process("P2", 2)
    p3 = Process("P3", 5)
    p4 = Process("P4", 6)

    # 프로세스 리스트
    processes = [p1, p2, p3, p4]

    # 라운드 로빈 생성, 퀀텀 설정
    RRS = RoundRobin(processes, quantum=1)
    RRS.run()

    # 시간 측정 종료
    finish = time.perf_counter()

    print(f'총 {round(finish - start, 4)}초 걸렸습니다')