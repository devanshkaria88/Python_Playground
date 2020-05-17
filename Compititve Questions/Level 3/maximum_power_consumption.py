"""
You are working in a HUGE Thermal Power Plant. The plant takes a lot of power.
Huge thermal power-plants takes even more power. To meet the plant's power needs, You boss has installed Solar Power
panels on the roof of the plant.But the plant is situated in the middle of a quasar quantum flux field, which wreaks
havoc on the solar panels. You and your team of engineers have been assigned to repair the solar panels, but you'd
rather not take down all of the panels at once if you can help it, since they do help power the power plant and all.

You need to figure out which sets of panels in any given array you can take offline to repair while still maintaining
the maximum amount of the power per array, AND to do that, you'll need to figure out what the maximum output of the
each array is. Write a Function solution(xs) that takes a list of integers representing the power output levels of
each panel in an array, and return the maximum product of some non-empty subset of those numbers. So for example,
if an array contained panels with power output levels of [2,-3,1,0,-5], the maximum product can be found by taking
subset: xs[0] = 2, xs[1] = -3 and xs[4] = -5, giving the product 2*(-3)*(-5) = 30. So solution([2,-3,1,0,-5])
would return 30.

::::::::::Examples:::::::::::

input = [1,2,-4,-31,4,1,-2,4,0,3]
output = 11904 (1*2*(-4)*(-31)*4*4*3]

==========TEST CASES===============

print(solution([2,-3,1,0,-5])) should return 30
print(solution([1,2,-4,-31,4,1,-2,4,0,3])) should return 11904
print(solution([6,-3,5])) should return 30
print(solution([0,0,0,0,4,-3])) should return 4
print(solution([1,2,4,-4,-2,-1])) should return 64
print(solution([5,6,7,-8,-6,-3])) should return 10080
"""
