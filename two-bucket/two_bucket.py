from copy import copy

"""
Since this mathematical problem is fairly subject to interpretation / individual approach, the tests have been written specifically to expect one overarching solution.

To help, the tests provide you with which bucket to fill first. That means, when starting with the larger bucket full, you are NOT allowed at any point to have the smaller bucket full and the larger bucket empty (aka, the opposite starting point); that would defeat the purpose of comparing both approaches!

Your program will take as input:
   - the size of bucket one
   - the size of bucket two
   - the desired number of liters to reach
   - which bucket to fill first, either bucket one or bucket two

More assumptions
   - assume we start with both buckets empty
   - assume size of bucket is an integer
   - assume the desired number of liter is an integer

Valid moves:
   - pouring from one bucket to another                  (transfer)
   - emptying one bucket and doing nothing to the other  (emptying)
   - filling one bucket and doing nothing to the other   (filling)

"""

class Bucket:
    VERB = False

    def __init__(self, cap):
        assert cap > 0
        self.cap = cap
        self.content = 0

    def filling(self):
        if self.content == self.cap:
            print("bucket already full!")
            return self
        if __class__.VERB: print(f"\t\tFilling bucket: {self} -> {self.cap}")
        self.content = self.cap
        return self

    def emptying(self):
        if self.content == 0:
            print("bucket already empty!")
            return self
        if __class__.VERB: print(f"\t\tEmptying bucket: {self} -> 0")
        self.content = 0
        return self

    def transfer(self, d_bucket):
        if self.is_full(d_bucket):
            if __class__.VERB: print("destination bucket already full!")
            return (self, d_bucket)

        elif self.is_empty():
            if __class__.VERB: print("src bucket is empty!")
            return (self, d_bucket)
        ##
        ## now: self.content < self.cap && d_bucket.content <= d_bucket.cap => transfer possible
        ##
        can_receive = d_bucket.cap - d_bucket.content
        #
        if can_receive > self.content:
            # can_receive > src_bucket content => update can_receive
            can_receive = self.content
            # then update dst / src accordingly
        #
        # now  can_receive <= d_bucket.content
        if __class__.VERB: print(f"\t\tTransfer from bucket: {self} to {d_bucket} of {can_receive} unit(s)")
        self.content -= can_receive
        d_bucket.content += can_receive
        return (self, d_bucket)

    def is_empty(self, d_bucket=None) -> bool:
        if d_bucket is None:
            return self.content == 0
        return d_bucket.content == 0

    def is_full(self, d_bucket=None) -> bool:
        if d_bucket is None:
            return self.content == self.cap
        return d_bucket.content == d_bucket.cap

    def goal_reached(self, goal: int):
        return self.content == goal

    def __str__(self):
        return f"c: {self.content}, cap: {self.cap}"


"""
  2 bucket B (big) S (Small)
  Starting with biggest bucket (B), transitions are:

  FB Fill B
  TB Transfer B -> S
  ES Empty Small

  Transitions are typically (starting from biggest):
   1     2         3            4
  FB -> TB -> is S full? yes:  ES  -> back to 2
              is S full? no: back to 1


  FS Fill $
  TS Transfer S -> B
  EB Empty Big

  Transitions are typically (starting from smallest):
   1     2         3           4
  FS -> TS -> is B full? yes: EB -> back to 2
              is B full? no: back to 1

  is the problem possible?
  - 1 <= goal < b1.cap + b2.cap
  - pgcd(B, C) != 1 only multiples of PGCD reachable

"""
class Problem:
    def __init__(self, b1: Bucket, b2: Bucket, goal: int, start: str):
        assert start == "one" or start == "two", "start must be 'one' or 'two'"
        self.b1, self.b2 = b1, b2
        assert 1 <=  goal <=  b1.cap + b2.cap, f"goal should satisfy: 0 <= {goal} <= {b1.cap + b2.cap}"
        self.goal, self.start = goal, start
        self.move = 0

    def solve(self, src, dst):
        gcd_ = gcd(self.b1.cap, self.b2.cap)

        if gcd_ != 1 and self.goal % gcd_ != 0:
            raise ValueError("goal {self.goal} is not reachable")

        # trivially reachable goals
        if self.goal == self.b1.cap:
            return (1, self.start, 0)

        elif self.goal == self.b2.cap:
            return (1, self.start, 0)

        elif self.goal == self.b1.cap + self.b2.cap:
            return (2, self.start, self.b2.content + self.b1.contant)

        if self.start == "one":
            return self.b2_strategy()
        else:
            # self.start == "two"
            return self.b1_strategy()

    def filling(self, b: Bucket):
        b.filling()

    def solution(self):
        #                         remaining in other bucket
        return (self.move, "one", self.b2.content) if self.b1.content == self.goal else \
            (self.move, "two", self.b1.content)

    def goal_reached(self) -> bool:
        return self.b1.content == self.goal or self.b2.content == self.goal or \
            self.b1.content + self.b2.content == self.goal

    def b1_strategy(self):
        """
        FS -> TS -> is N full? yes:  EB  -> back to 2
                    is B full? no: back to 1
        """
        nextop = "filling"
        while not self.goal_reached():
            if nextop == "filling":
                self.filling(self.b2)
                self.move += 1
                nextop = "transfer"

            if nextop == "transfer":
                self.move += 1
                self.b2.transfer(self.b1)

            if self.goal_reached(): break

            if self.b1.is_full():
                self.b1.emptying()
                self.move += 1
                next_op = "transfer"
            else:
                nextop = "filling"
        #
        # print(f"\n\tFINAL STATE: <{self.b1} / {self.b2}> - start was: {self.start}")
        return self.solution()

    def b2_strategy(self):
        """
        FB -> TB -> is S full? yes:  ES  -> back to 2
                    is S full? no: back to 1
        """
        nextop = "filling"
        while not self.goal_reached():
            if nextop == "filling":
                self.filling(self.b1)
                self.move += 1
                nextop = "transfer"

            if nextop == "transfer":
                self.move += 1
                self.b1.transfer(self.b2)

            if self.goal_reached(): break

            if self.b2.is_full():
                self.b2.emptying()
                self.move += 1
                next_op = "transfer"
            else:
                nextop = "filling"
        #
        # print(f"\n\tFINAL STATE: <{self.b1} / {self.b2}> - start was: {self.start}")
        return self.solution()

def gcd(x: int, y: int) -> int:
    """
    assume x > 0 and y > 0
    """
    x, y = (y, x) if x < y else (x, y)
    if y == 0: return x
    r = x
    while r > 1:
        r = x % y
        x, y = y, r
    #
    return x if r == 0 else r

#
def measure(bucket_one: int, bucket_two: int, goal: int, start_bucket: str):
    assert start_bucket == "one" or start_bucket == "two", "start_bucket must be 'one' or 'two'"

    b1 = Bucket(bucket_one)
    b2 = Bucket(bucket_two)
    pb = Problem(b1, b2, goal, start_bucket)
    return pb.solve(b1, b2)
