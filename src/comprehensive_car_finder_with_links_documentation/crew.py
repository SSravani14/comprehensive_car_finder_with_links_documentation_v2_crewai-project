import os
from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import (
	SerperDevTool,
	BrowserbaseLoadTool
)



@CrewBase
class ComprehensiveCarFinderWithLinksDocumentationCrew:
    """ComprehensiveCarFinderWithLinksDocumentation crew"""

    
    @agent
    def customer_requirements_specialist(self) -> Agent:
        
        return Agent(
            config=self.agents_config["customer_requirements_specialist"],
            tools=[

            ],
            reasoning=False,
            inject_date=True,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
        )
    
    @agent
    def automotive_market_analyst(self) -> Agent:
        
        return Agent(
            config=self.agents_config["automotive_market_analyst"],
            tools=[
				SerperDevTool(),
				BrowserbaseLoadTool()
            ],
            reasoning=False,
            inject_date=True,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
        )
    
    @agent
    def automotive_appraiser(self) -> Agent:
        
        return Agent(
            config=self.agents_config["automotive_appraiser"],
            tools=[
				SerperDevTool(),
				BrowserbaseLoadTool()
            ],
            reasoning=False,
            inject_date=True,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
        )
    
    @agent
    def vehicle_inspection_manager(self) -> Agent:
        
        return Agent(
            config=self.agents_config["vehicle_inspection_manager"],
            tools=[
				SerperDevTool()
            ],
            reasoning=False,
            inject_date=True,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
        )
    
    @agent
    def automotive_legal_compliance_specialist(self) -> Agent:
        
        return Agent(
            config=self.agents_config["automotive_legal_compliance_specialist"],
            tools=[
				SerperDevTool(),
				BrowserbaseLoadTool()
            ],
            reasoning=False,
            inject_date=True,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
        )
    

    
    @task
    def process_buyer_specifications(self) -> Task:
        return Task(
            config=self.tasks_config["process_buyer_specifications"],
        )
    
    @task
    def research_market_pricing_for_specifications(self) -> Task:
        return Task(
            config=self.tasks_config["research_market_pricing_for_specifications"],
        )
    
    @task
    def search_vehicles_with_specifications(self) -> Task:
        return Task(
            config=self.tasks_config["search_vehicles_with_specifications"],
        )
    
    @task
    def evaluate_vehicle_values(self) -> Task:
        return Task(
            config=self.tasks_config["evaluate_vehicle_values"],
        )
    
    @task
    def create_inspection_plans(self) -> Task:
        return Task(
            config=self.tasks_config["create_inspection_plans"],
        )
    
    @task
    def documentation_and_security_requirements(self) -> Task:
        return Task(
            config=self.tasks_config["documentation_and_security_requirements"],
        )
    
    @task
    def generate_top_10_vehicle_recommendations_summary(self) -> Task:
        return Task(
            config=self.tasks_config["generate_top_10_vehicle_recommendations_summary"],
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the ComprehensiveCarFinderWithLinksDocumentation crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
