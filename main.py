from firebase import firebase

from next_generation import NextGen

fb = None

data = None

def main():

    global fb

    global data

    fb = firebase.FirebaseApplication("https://alexa-feed-me.firebaseio.com/", None)

    data = fb.get('users', None)

    users = list(data.keys())

    for user in users:

        article_text = process_user(user)

        user_path = 'users/' + user

        fb.put(user_path, 'article', article_text)


def process_user(user_id):

    global data

    similarity_processor = NextGen(data[user_id]['article'], data[user_id]['query'])

    information_to_update = similarity_processor.convert_relevant_words_article()

    return information_to_update


def main1():

    corpus = 'The White House is increasingly at odds with congressional Republicans over the party’s health-care message for the 2020 election campaign.  A growing number of Republicans in Congress want to focus on transparency, competition and other free-market solutions to rising costs, all as part of their platform for 2020. But Trump administration officials are taking steps to invalidate the Affordable Care Act, including a move this week to help scuttle the law through the courts.  Shaping the Trump administration strategy to dismantle the ACA are a handful of key White House policy advisers who have the ear of the president, including acting chief of staff Mick Mulvaney, according to multiple people familiar with the matter. They are also impeding some initiatives by Health and Human Services designed to lower drug pricing, the people said.  For years, Republicans rallied around efforts to repeal the ACA. But the law is now a crucial part of the nation’s health-care economy, upon which millions of voters rely for coverage. The discontent among the GOP’s congressional caucus reflects a reality that without something to take its place, the ACA can no longer be scrapped without significant political damage to anybody who disrupts its coverage.  Sen. Susan Collins (R., Maine), facing a competitive challenge in 2020, said she is “vehemently opposed” to the White House efforts to dismantle the ACA in the courts.  “The president is very clear that he understands the importance of health care,” said Ms. Collins, who cast a key vote against the GOP effort to kill the ACA in 2017. “In order to do that, he has to have a detailed plan that is going to be an improvement over the ACA.”  Newsletter Sign-up  As of Wednesday, it was difficult to find anyone on Capitol Hill who could say how such an improvement might take shape, a fact that Democrats were quick to note. “The American public spoke loud and clear in the November 2018 elections, and addressed the Republican antics by defeating them resoundingly,” said Senate Minority Leader Chuck Schumer (D., N.Y.) on the Senate floor Wednesday.  “Now, the president wants to go back to repeal and replace again?” Mr. Schumer added. “Make our day.”  Marc Short, chief of staff to Vice President Mike Pence, said Wednesday on MSNBC that the administration will come out with a plan to replace the ACA in coming months.  Democrats have their own messaging challenges over health care. The dispute between Republicans and the White House has gotten less attention than a similar tug of war between Democrats who are divided over how to respond to growing calls, from the party’s progressive wing, for a federally run health system, or Medicare for All.  Rather than try to repeal the ACA, many Republicans want to counter the Democrats’ calls for a bigger government health-care role with a free-market message revolving around greater transparency, more choices for consumers, and competition—in hopes such policies would lower the cost of coverage.  The White House threw its weight behind a lawsuit, currently winding through the appeals process, that seeks to kill the ACA. That case argues the ACA is no longer valid now that the GOP tax package last year ended a mandate that individuals without coverage pay a penalty, a source of revenue that was part of the original ACA.  The case “needs to be dropped completely, even if it means we have to eat crow,” said Sen. Mike Braun (R., Ind.) in an interview Wednesday.   After Mueller Report: Washingtons Hard Pivot to Health Care After Mueller Report: Washingtons Hard Pivot to Health Care With special counsel Robert Muellers investigation concluded, House Democrats and the Trump administration have quickly shifted focus to a different issue: Health care. WSJs Gerald F. Seib explains. Photo: Getty Mr. Trump on Wednesday doubled down on his attack on the ACA, the signature achievement of his predecessor, Barack Obama. “If the Supreme Court rules that Obamacare is out,” he told reporters in the Oval Office, “we’ll have a plan that is far better than Obamacare.”  Besides Mr. Mulvaney, others advising the White House include Joe Grogan, who heads the Domestic Policy Council, and who has taken a lead role in driving actions to temper drug-pricing proposals that some Republicans are eager to see, according to a person familiar with White House deliberations. Mr. Grogan and his colleagues have also sought to curb a proposal to curtail millions of dollars in annual rebates that drugmakers give to middlemen known as pharmacy-benefit managers in Medicare, they said.  These policy positions have caused tensions leading to yelling arguments between Mr. Grogan and HHS Secretary Alex Azar, said people with knowledge of the altercations.  RELATED Trump Administration Renews Attempt to Topple Affordable Care Act (March 26) Democrats Signal Renewed Focus on Health Care After Mueller Findings (March 26) Affordable Care Act Sign-Ups Total 11.4 Million for This Year (March 25) House Democrats Reveal Plan for Medicare for All (Feb. 26) The White House didn’t respond to emails seeking comment.  House Republicans say they see the administration’s strategy as applying pressure on Congress to force them to come up with a legislative solution. “I just don’t think that’s the right way to go,” said Rep. Tom Reed (R., N.Y.), co-chairman of a bipartisan group of House lawmakers. “That puts a lot of Americans in harm’s way.”  Voters are skeptical of their efforts after their monthslong quest to roll back the ACA in 2017 that sputtered to a stop when Republicans couldn’t reach a consensus, many GOP members said.  “The American people don’t believe we have an offering because of what happened two years ago,” said Rep. Patrick McHenry of North Carolina, the top Republican on the Financial Services Committee. But Republicans can’t go into the 2020 election cycle without a proposal, he said.  “Us not having a pro-active conviction on health-care policy is a problem,” he said. “A fixable one.”'

    query = 'obamacare'

    w = NextGen(corpus, query)

    print(w.convert_to_text())

main()
