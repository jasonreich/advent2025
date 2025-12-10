from pulp import LpVariable, LpProblem, LpMinimize, LpStatus, PULP_CBC_CMD
import re

example = """
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
""".strip()

with open("10/input.txt") as f:
    from_file = f.read()

line_re = re.compile("\\[([.#]+)\\](( \\([0-9,]+\\))+) \\{([0-9,]+)\\}")

type Problem = tuple[list[int], list[list[int]], list[int]]

def parse_line(line: str) -> Problem:
    if first_parse := line_re.match(line):
        (indicators_input, buttons_input, _, joltage_input) = first_parse.groups()
        indicators = [ 1 if c == '#' else 0 for c in indicators_input ]
        buttons = [
            [
                int(light)
                for light in button[:-1].split(',')
            ]
            for button in buttons_input.split(' (')
            if button != ''
        ]
        return (indicators, buttons, [])
    else:
        raise RuntimeError("Could not parse")
    
def solve(problem: Problem) -> int:
    (indicator_final, button_config, _) = problem
    
    on_offs = LpVariable.dict(
        "on_offs",
        range(len(indicator_final)),
        lowBound=0,
        cat = 'Integer'
    )
    
    button_presses = LpVariable.dict(
        "button_presses", 
        range(len(button_config)), 
        lowBound=0,
        cat = 'Integer'
    )
    
    prob = LpProblem("AdventProblem", LpMinimize)
    
    for i, state in enumerate(indicator_final):
        prob += sum([
            button_presses[j]
            for j, bc in enumerate(button_config)
            if i in bc
        ]) == state + 2 * on_offs[i]
        
    prob += sum([ button_presses[j] for j in range(len(button_config)) ])
    
    status = prob.solve(PULP_CBC_CMD(msg=0))
    return sum([ v.value() for v in button_presses.values()])
        

print(sum([
    solve(parse_line(line))
    for line in from_file.splitlines()
]))

# x = LpVariable("x", 0, 3)
# y = LpVariable("y", cat="Binary")

# prob = LpProblem("myProblem", LpMinimize)

# prob += x + y <= 2
# prob += -4*x + y


# status = prob.solve(PULP_CBC_CMD(msg=0))
# print(LpStatus[status])
# print(x.value())