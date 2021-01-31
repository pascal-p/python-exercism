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
    def __init__(self, cap):
        assert cap > 0
        self.cap = cap
        self.content = 0

    def filling(self):
        if self.content == self.cap:
            print("bucket already full!")
            return self
        print(f"\t\tFilling bucket: {self} -> {self.cap}")
        self.content = self.cap
        return self

    def emptying(self):
        if self.content == 0:
            print("bucket already empty!")
            return self
        print(f"\t\tEmptying bucket: {self} -> 0")
        self.content = 0
        return self

    def transfer(self, d_bucket):
        if self.is_full(d_bucket):
            print("destination bucket already full!")
            return (self, d_bucket)

        elif self.is_empty():
            print("src bucket is empty!")
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
        print(f"\t\tTransfer from bucket: {self} to {d_bucket} of {can_receive} unit(s)")
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


class Problem:
    All_Actions = {'transfer', 'emptying', 'filling'} ## set

    def __init__(self, b1: Bucket, b2: Bucket, goal: int, start: str):
        assert start == "one" or start == "two", "start must be 'one' or 'two'"
        self.b1, self.b2 = b1, b2
        self.goal, self.start = goal, start
        self.move = 0
        #
        self.last_action = None
        self.b_action = None # the bucket (dst) onto which last action was performed
        self.pending = None
        self.visited = []    # keep track of visited state to avoid cycle
        self.ix = 0

    def solve(self, src, dst, action=None):
        if self.last_action is None:
            print("FIRST S O L V E ...")
            # first action ever...
            if self.start == "one":
                self.filling(self.b1)
                self.b_action = self.b1
            else:
                # self.start == "one"
                self.filling(self.b2)
                self.b_action = self.b2
            #
            self.last_action = "filling"
            self.move = 1
            return self.action()

        elif self.goal_reached():
            print("================================= G O A L  R E A C H E D =========================")
            return True

        else:
            # exec. next action
            if action == "transfer":
                src.transfer(dst)

            elif action == "emptying":
                dst.emptying()

            else:
                dst.filling()

            print(f"S O L V E ... state (updated): {self.b1} // {self.b2}")                
            self.last_action = action
            self.b_action = dst
            self.move += 1
            return self.action()
            
    def action(self):
        poss_actions = self.possible_actions()
        print(f"A C T I O N ... possible actions are: {poss_actions} / move: {self.move} / state: <{self.b1}, {self.b2}>")
        self.ix += 1
        if self.ix == 10:
            print("STOP...")
            return False
        
        assert not(self.b1.is_empty() and self.b2.is_empty()), "both bucket cannot be empty - this was the init state!"        

        for action in poss_actions:
            state = {
                "b1": copy(self.b1),
                "b2": copy(self.b2),
                "move": self.move,
                "last_action": self.last_action
            }
            src, dst = None, None
            
            # do_next action, conditionally on previous action (self.last_action)
            if self.b_action == self.b1:
                src, dst, action = self.action_for(action, new_dst=self.b2)
                if action is None: continue
            ##
            elif self.b_action == self.b2:
                src, dst, action = self.action_for(action, new_dst=self.b1)
                if action is None: continue

            else:
                assert self.b_action is not None, f"b_action {self.b_action} MUST be defined, got None"
            
            print(f"\tTRYING action {action}")    
            while True:
                self.solve(src, dst, action)
                
                if self.goal_reached():
                    print(f"\tPOST RECURSION 2...")
                    return True

                v_state = {"src": src, "dst": dst, "action": action}
                if not self.find_visited(v_state):
                    self.visited.append(v_state)

                # failure => backtrack
                self.b1 = state["b1"]
                self.b2 = state["b2"]
                self.move = state["move"]
                self.last_action = state["last_action"]

                # is there a pending action
                if self.pending is not None:
                    src, dst = self.pending['new_src'], self.pending['new_dst']
                    self.pending = None
                    print(f">> PENDING action: {action} / src: {src} / dst: {dst}")
                    ## Go back to solve(...)
                else:
                    break
        ## TODO: try again inverting src and dst bucket !! HOW? / NOT REQUIRED...
        return False

    def filling(self, b: Bucket):
        b.filling()

    def possible_actions(self):
        return list(__class__.All_Actions - set([self.last_action]))

    def solution(self):
        # need to tell wich bucket reached the goal
        gb = self.goal_for()
        return (self.move, "one" if gb == self.b1 else "two", self.b2.content if gb == self.b1 else self.b1.content)

    def goal_reached(self) -> bool:
        return self.b1.content == self.goal or self.b2.content == self.goal

    def goal_for(self):
        return self.b1 if self.b1.content == self.goal else self.b2

    def find_visited(self, state) -> bool:
        for _state in self.visited:
            if _state.src != satte.src or _satte.dst != state.dst or \
               _state.action != state.action:
                return False
        return True

    def action_for(self, action, new_dst):
        src = self.b2 if new_dst == self.b1 else self.b1
        if self.last_action == "filling":
            if action == 'filling':
                return (src, new_dst, action)  ## next (dst) bucket will be new_dst

            elif action == 'emptying':
                if new_dst.is_empty(): return (None, None, None) ## go straight to next available action
                ##                                 ## because no point...
                else: ## not new_dst.is_empty() => we can empty new_dst
                    return (src, new_dst, action)  ## next (dst) bucket will be new_dst
                    ## NOTE: now emptying bq is pointless as we just filled it

            elif action == 'transfer':
                ## 2 possibilities here:
                ##   - transfer(b1 -> b2) if b1.content > 0 && b2.content < b2.cap
                ##   - transfer(b2 -> b1) if b2.content > 0 && b1.content < b1.cap
                ##
                ## FIXME: Naming is not really good here...
                if not src.is_empty() and not new_dst.is_full():
                    self.pending = {'new_src': new_dst, 'new_dst': src}
                    return (src, new_dst, action)
                    #
                elif not new_dst.is_empty() and not src.is_full():
                    src, new_dst = new_dst, src    ## swap!
                    self.pending = {'new_src': src, 'new_dst': new_dst}
                    return (src, new_dst, action)
                    #
                else:
                    return (None, None, None)

        elif self.last_action == "transfer":  ## Ex. transfer b2(src: new_dst) -> b1 (dst: src)
            if action == 'filling':
                ## filling b2/new_dst is possible
                self.pending = {'new_src': new_dst, 'new_dst': src}
                return (src, new_dst, action)

                ## filling b1/ is possible if b1 not full
                src, new_dst = new_dst, src    ## swap!
                return (src, new_dst, action)

            elif action == 'emptying':
                ## emptying b1/src is possible iff b1/src is not full
                if not src.is_full() and not new_dst.is_empty():
                    print(f"11111111111 / bucket: {src}")
                    src, new_dst = new_dst, src    ## swap!
                    self.pending = {'new_src': src, 'new_dst': new_dst}
                    return (src, new_dst, action)

                ## emptying b2 is possible iff b2 not empty and we do not end up with both bucket empty!
                if not new_dst.is_empty():
                    print("22222222222")
                    return (src, new_dst, action)
                else:
                    return (None, None, None)

            elif action == 'transfer':
                return (None, None, None)     ## cannot do 2 transfer in a row

        elif self.last_action == "emptying":  ## Ex. emptying b1
            if action == 'filling':
                ## filling b1 is possible iff b1 was not full when emptied? How to we know this?
                ## by checking the (already) visited state
                ##
                self.pending = {'new_src': src, 'new_dst': new_dst}  ## filling b2 is possbile iff b2 is not full
                src, new_dst = new_dst, src    ## swap!
                return (src, new_dst, action)

            elif action == 'emptying':
                return (None, None, None)     ## NO-OP or return to init. state

            elif action == 'transfer':
                ## only possible from b2 -> b1 as we emptied b1
                return (src, new_dst, action)
        #
        return (None, None, None)

#
def measure(bucket_one: int, bucket_two: int, goal: int, start_bucket: str):
    assert start_bucket == "one" or start_bucket == "two", "start_bucket must be 'one' or 'two'"

    b1 = Bucket(bucket_one)
    b2 = Bucket(bucket_two)
    pb = Problem(b1, b2, goal, start_bucket)

    if pb.solve(b1, b2) is not None:
        return pb.solution()
    else:
        return None # no solution
#
# assert transfer(src_bucket=2, src_cap=3, dst_bucket=4, dst_cap=5) == (1, 5)
# assert transfer(src_bucket=3, src_cap=3, dst_bucket=4, dst_cap=5) == (2, 5)
# assert transfer(src_bucket=1, src_cap=3, dst_bucket=0, dst_cap=5) == (0, 1)
# assert transfer(src_bucket=0, src_cap=3, dst_bucket=5, dst_cap=5) == (0, 5)
# assert transfer(src_bucket=2, src_cap=3, dst_bucket=1, dst_cap=5) == (0, 3)
# assert transfer(src_bucket=0, src_cap=3, dst_bucket=4, dst_cap=5) == (0, 4)
#
