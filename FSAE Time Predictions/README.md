# FSAE Time Predictions

### Context
**Formula SAE** is a competition where students design and build formula-style race cars, and compete against teams from other universities from around the world.
Two parts of the competition, Acceleration and Skidpad, aim to test the straight-line acceleration and steady-state cornering abilities of the cars, respectively.

**Acceleration** starts from a standstill, and measures the elapsed time to travel 75 meters.
Reaction time is not measured, and cars are allowed about 0.3 meters of rollout before the first timing gate.

**Skidpad** starts from a standstill, and measures the average elapsed time to complete a full left-hand and right-hand circle with a 15.25 meter inner diameter.
Reaction time is not measured, and cars must complete two consecutive circles in each direction. Only the second full circle in either direction is timed
in order to emulate a steady-state condition as closely as possible.

### Problem Definition
The goal of this exercise is develop a model to correlate an FSAE car's basic specifications (weight, engine size & configuration, etc.) to an expected best time
in the Acceleration and Skidpad events.

This model may be useful to teams in the initial design phase of their competition cycle. The vehicle characteristics that are considered by this model are deeply-rooted
in a vehicle's design, and must be chosen early in the design process. Making an informed decision about these characteristics can be difficult,
especially for new teams who have limited experience and validation data from previous years.

It may also be useful to experienced teams who would like to explore the effects of changing key aspects of their design philosophy. Each team has a different
(and constantly changing) set of priorities that they believe will give them the best competition result. This model may be used to see how a team's performance
in these events may change if they change their engine configuration, or shed 10 kilos.

I will be using [data from previous competitions](https://www.sae.org/attend/student-events/formula-sae-michigan/awards-results) ranging from 2013-2019
published by the organizers of the competition, SAE International.

### Limitations
- This model currently does not consider any tire, suspension, or aerodynamic characteristics, all of which have significant effects on performance in these events.
- It does not consider rule changes across years, the most significant one being the post-2014 aero rules to
[limit wing sizes](https://lh3.googleusercontent.com/-hC25U7Wc-OA/U3g6hhkxwqI/AAAAAAAASUE/DwGIFiQCG2M/w1303-h869-no/DSC01355.JPG).
- It does not account for variations in driver skill. I chose to focus on acceleration and skidpad because they requrie the least driver skill,
but the effects of these variations may still be present in the model.
- Finally, this model may not perform well outside the envelope of normal FSAE vehicle characteristics. For example, most cars weigh between 130 and 230 kilos,
so you may not be able to accurately predict what would happen if your car weighed 50 or 500 kilos.
