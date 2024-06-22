#!/usr/bin/env python3

import sys
import random
import numpy as np
from routes import values

dt = np.dtype([("corp_start", "S10"), ("corp_end", "S10"), ("distance", int)])
data_set = np.array(values, dtype=dt)


def all_corps():
    corps = {}
    corp_set = set(data_set["corp_end"])
    for corp in corp_set:
        corps[corp] = ""
    return corps


def randomize_corp_start(corps):
    return random.choice(corps)


def get_shortest_route(routes):
    route = sorted(routes, key=lambda dist: dist[2]).pop(0)
    return route


def greedy_path(verbose=False):
    start_corp = randomize_corp_start(list(all_corps().keys()))
    print(f"시작회사: {start_corp}")
    
    itinerary = []
    corps_visited = {}
    count = 1
    while True:
        possible_routes = []
        if verbose:
            print("------")
            print(f"회사 {start_corp} 에서 갈 수 있는 회사들:")
        for path in data_set:
            if start_corp in path["corp_start"]:
                # 한 번 방문했던 회사는 다시 방문할 수 없음.
                if path["corp_end"] in corps_visited:
                    continue
                else:
                    if verbose:
                        print(f"{path}", end=", ")
                    possible_routes.append(path)
        if not possible_routes:
            if verbose:
                print("더 이상 갈 수 있는 회사가 없습니다. 여행을 종료합니다.")
                print("------")
            break
        # 다음으로 방문할 수 있는 회사들 중에서 가장 짧은 거리의 회사를 선택합니다.
        route = get_shortest_route(possible_routes)
        if verbose:
            print(f"\n다음 여정: {route} ({count} 번째 동선입니다)")
        count += 1
        itinerary.append(route)
        # 방문한 회사를 기록합니다.
        corps_visited[route[0]] = count
        if verbose:
            print(f"방문한 회사들: {corps_visited}")
            print(f"현재까지의 여정: {itinerary}")
        start_corp = route[1]

    return itinerary


def get_total_distance(complete_itinerary):
    distance = sum(z for x, y, z in complete_itinerary)
    return distance


def lowest_simulation(num):
    routes = {}
    for _ in range(num):
        itinerary = greedy_path()
        distance = get_total_distance(itinerary)
        print(f"총 거리: {distance}")
        routes[distance] = itinerary
    shortest_distance = min(routes.keys())
    route = routes[shortest_distance]
    return shortest_distance, route


def main():
    # print(f"전체 경로:\n{data_set}")
    if len(sys.argv) == 2:
        iterations = int(sys.argv[1])
        print(f"{iterations}회 시뮬레이션을 실행합니다.")
        distance, route = lowest_simulation(iterations)
        print(f"최단거리: {distance}")
        print(f"최적경로: {route}")
    else:
        itinerary = greedy_path(verbose=True)
        print(f"동선: {itinerary}")
        print(f"총거리: {get_total_distance(itinerary)}")


if __name__ == "__main__":
    main()