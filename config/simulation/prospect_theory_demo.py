# -*- coding: utf-8 -*-
"""
This simulation setup demonstrates the concepts of Prospect Theory
as described in the following papers:

	Prospect theory: An analysis of decision under risk.
	Kahneman, Daniel; Tversky, Amos
	Moser, Paul K. (Ed), (1990). Rationality in action:
	Contemporary approaches. , (pp. 140-170).
	New York, NY, US: Cambridge University Press, vi, 493 pp.

	A perspective on judgment and choice: Mapping bounded rationality.
	Kahneman, Daniel
	American Psychologist, Vol 58(9), Sep 2003, 697-720.
	doi: 10.1037/0003-066X.58.9.697

Created on Tue Dec 17 13:54:42 2013

@author: 7yl4r
"""

from behaviorSim.PECSagent.agent import agent
import behaviorSim.API as API

import copy

def configure(sim):

	# set up the question(s)
	#TODO: question should include prospect of outcomes, ... MORE
	class questionIterator(object):
		'''
		This class returns the current question being posed.
		'''
		def __init__(self):
			self.currentQuestionN = 0
			self.currentQuestion  = None

			self.questions = [[2500,.33,2400,.66,0,.01],
			                  [2500,.33,0   ,.67],
			                  [4000,.8 ,3000],
			                 ]

		def __call__(self,t,agent):
			# update question if agent has competed last question
			if agent.behavior.choice(t) != None:
				self.currentQuestionN += 1
				self.currentQuestion = self.getQuestion()
			return self.currentQuestion

		def getQuestion(self):
			n = self.currentQuestionN
			if n<1:
				raise ValueError('question # cannot be negative')
			elif n == 1:
				self.currentQuestion = []
			elif n == 2:
				self.currentQuestion = []
			else:
				raise ValueError('question #'+str(n)+' not found')
			return self.currentQuestion

	currentQuestionProspect = API.getConstruct('currentQuestionProspect'
		,questionIterator)
	# this should be None when there is no prospect question posed,
	# if there is a question it is a list



	API.addFeature(environment,time,)

	#sim.environment.???
	API.addEvent(environment,time, gamblePrompt)

	# create rational agent
	rationalAgent = agent(sim.environment)

	class event:
		if time == timeTrigger:
			triggerEvent(environment)

	prospect = API.getConstruct('prospect'
		,getProspectFromEnvironment
		,environment.currentQuestionProspect)
	API.addConstruct(rationalAgent.context,prospect)





	def expectation(prospect):
		'''
		returns expectation value for given set of probabilities
		t = time
		prospect = list of outcome and probability pairs (x_1,p_1,x_2,p_2...x_n,p_n)
		'''
		sum = 0
		for i in range(int(len(prospect)/2)):
			sum += prospect[i*2]*prospect[i*2+1]

		return sum

#TODO:	def utilityOfAssets(assetPosition)
#TODO: 	def assetIntegration(prospect,assetPosition):
#TODO:	def riskAversionAssetUtility(assetPosition):
#			''' this is a concave function of assetPosition '''

	expectation = API.getConstruct('expectation'
		,calculateExpectationValue
		,rationalAgent.context.prospect)

	API.addConstruct(rationalAgent.state,expectationValue)


	# create a classically risk-averted agent
	riskAvertedAgent = copy.deepcopy(rationalAgent)


	# create a more realistic human agent by extending the rational agent
	prospectTheoryAgent = copy.deepcopy(rationalAgent)

