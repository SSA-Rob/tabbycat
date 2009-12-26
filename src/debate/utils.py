def pair_list(ls):
    half = len(ls)/2
    return zip(ls[:half], ls[half:])

def generate_random_results(round):
    from debate.models import Debate, DebateResult
    import random

    debates = Debate.objects.filter(round=round)

    for debate in debates:
        dr = DebateResult(debate)
        
        for team in ('aff', 'neg'):
            speakers = getattr(debate, '%s_team' % team).speakers
            for i in range(1, 4):
                dr.set_speaker_entry(
                    team = team,
                    pos = i,
                    speaker = speakers[i - 1],
                    score = random.randint(60,80)
                )
            dr.set_speaker_entry(
                team = team,
                pos = 4,
                speaker = speakers[0],
                score = random.randint(30,40)
            )

        dr.save()
        debate.result_status = debate.STATUS_CONFIRMED
        debate.save()

        
def test_gen():
    from debate.models import Round
    generate_random_results(Round.objects.get(pk=1))

