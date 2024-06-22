import optparse
import decimal
import sys


class Algorithm():
    
    MINIMAL_FACE_VALUE = 10

    def __init__(self, money, coin_types, verbose=False):
        self.money = money
        self.verbose = verbose
        self.coin_types = coin_types
        assert min(self.coin_types) == Algorithm.MINIMAL_FACE_VALUE, \
            f"최소 동전단위는 {Algorithm.MINIMAL_FACE_VALUE}원입니다."
        self.cache = self.coin_types.copy()

    def _recursive_change(self, remainder):
        if len(self.coin_types) == 0:
            return []
        max_face_value = max(self.coin_types)
        self.coin_types.remove(max_face_value)
        n, remainder = divmod(remainder, max_face_value)
        if self.verbose:
            print(f"{max_face_value}원 짜리 동전 {n}개")
        return [n] + self._recursive_change(remainder)

    def calculate(self):
        result = self._recursive_change(self.money)
        self.coin_types = self.cache.copy()
        return result


def controller():
    p = optparse.OptionParser(
        description="탐욕 알고리즘을 이용한 잔돈 반환법 계산",
        usage="python3 %prog [잔돈] (optional)[플래그]")

    p.add_option("--print", "-p",
                action="store_true",
                help="연산 결과를 출력합니다.")

    options, arguments = p.parse_args()
    if not arguments:
        p.print_help()
        sys.exit(1)
    
    money = arguments[0]
    try:
        money = decimal.Decimal(money)
        if float(money) < 0:
            raise ValueError("잔돈은 0보다 작을 수 없습니다.")
        if float(money) % Algorithm.MINIMAL_FACE_VALUE != 0:
            raise ValueError(f"{Algorithm.MINIMAL_FACE_VALUE}원 단위로 입력해주세요.")
        money = int(money)
    except ValueError as e:
        print(e)
        sys.exit(1)
    except decimal.InvalidOperation:
        print("잘못된 입력입니다.")
        sys.exit(1)
    else:
        return money, options.print


def main():
    money, verbose = controller()
    alg = Algorithm(money, coin_types={10, 50, 100, 500}, verbose=verbose)
    _ = alg.calculate()


if __name__ == "__main__":
    main()