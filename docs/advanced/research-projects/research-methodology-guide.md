# Research Methodology for Robotics & Unmanned Systems

A practical guide to conducting rigorous, reproducible research in unmanned vehicle systems.

## The Scientific Method in Robotics

### 1. Observation & Question
- Identify problem or phenomenon
- Formulate specific research question
- Ensure question is testable and answerable

### 2. Background Research
- Comprehensive literature review
- Understand current state-of-the-art
- Identify gaps and opportunities

### 3. Hypothesis Formation
- Propose possible answer or solution
- Make testable predictions
- Define success criteria

### 4. Experimental Design
- Plan systematic tests
- Control variables
- Ensure reproducibility

### 5. Data Collection
- Execute experiments rigorously
- Document thoroughly
- Maintain integrity

### 6. Analysis
- Process and visualize data
- Apply statistical methods
- Interpret results objectively

### 7. Conclusion
- Answer research question
- Compare to hypothesis
- Discuss limitations and future work

### 8. Communication
- Write papers/reports
- Present findings
- Peer review and publication

## Experimental Design

### Types of Experiments

**Comparative Studies**
- Compare approach A vs approach B
- Control all other variables
- Statistical significance testing

**Ablation Studies**
- Remove components systematically
- Show contribution of each part
- Justify design decisions

**Parameter Studies**
- Vary parameters systematically
- Find optimal settings
- Understand sensitivity

**Scalability Studies**
- Test with varying problem sizes
- Show how approach scales
- Identify bottlenecks

**Robustness Studies**
- Test under varied conditions
- Add noise and disturbances
- Evaluate failure modes

### Designing Good Experiments

**Key Principles**:

1. **Controlled Variables**: Change one thing at a time
2. **Sufficient Trials**: Enough data for statistics (n≥30)
3. **Randomization**: Avoid systematic biases
4. **Blinding**: When possible, remove experimenter bias
5. **Reproducibility**: Others can replicate

**Common Pitfalls**:

- Too few trials (statistical power)
- Cherry-picking best results
- Not testing failure cases
- Overfitting to test scenarios
- Ignoring confounding variables

## Data Collection Best Practices

### Before Collection

- **Test equipment**: Ensure everything works
- **Calibrate sensors**: Document calibration data
- **Prepare environment**: Control variables
- **Pilot runs**: Test procedure
- **Document protocol**: Write down exact steps

### During Collection

- **Systematic approach**: Follow protocol exactly
- **Real-time notes**: Record observations
- **Label everything**: Clear file naming
- **Save raw data**: Never overwrite originals
- **Backup frequently**: Redundant storage

### After Collection

- **Initial inspection**: Check for obvious errors
- **Data validation**: Verify completeness
- **Organization**: Logical directory structure
- **Metadata**: Document collection conditions
- **Backup**: Multiple locations

### Data Organization

```
project/
├── data/
│   ├── raw/              # Original data (read-only)
│   │   ├── trial_001/
│   │   ├── trial_002/
│   │   └── ...
│   ├── processed/        # Cleaned/processed data
│   ├── analysis/         # Analysis results
│   └── README.md         # Data description
├── code/
│   ├── collection/       # Data collection scripts
│   ├── processing/       # Data processing
│   └── analysis/         # Analysis code
├── docs/
│   ├── protocol.md       # Experimental protocol
│   ├── notes/            # Lab notebook entries
│   └── results/          # Figures and tables
└── README.md
```

## Statistical Analysis

### Descriptive Statistics

Report these for key metrics:
- **Mean**: Average value
- **Median**: Middle value
- **Standard deviation**: Spread
- **Min/Max**: Range
- **Quartiles**: Distribution shape

### Visualization

**Box Plots**: Show distribution and outliers
**Scatter Plots**: Relationships between variables
**Line Plots**: Trends over time or parameters
**Bar Charts**: Comparisons between conditions
**Heatmaps**: 2D parameter spaces

### Hypothesis Testing

**t-tests**: Compare two conditions
**ANOVA**: Compare multiple conditions
**Chi-square**: Categorical data
**Non-parametric tests**: When assumptions violated

### Effect Size

Don't just report significance (p-value), report:
- **Magnitude**: How big is the difference?
- **Confidence intervals**: Range of likely values
- **Practical significance**: Does it matter in practice?

### Common Mistakes

- P-hacking (trying many tests until one works)
- Not correcting for multiple comparisons
- Confusing correlation with causation
- Ignoring effect size
- Not checking assumptions (normality, etc.)

## Simulation vs Real-World Testing

### When to Use Simulation

**Advantages**:
- Safe and cheap
- Rapid iteration
- Perfect ground truth
- Controlled conditions
- Systematic parameter sweeps

**Disadvantages**:
- Reality gap
- Model inaccuracies
- Missing complexity
- False confidence

### When to Use Real Hardware

**Essential for**:
- Final validation
- Unexpected effects
- User studies
- Safety testing
- Real-world conditions

**Challenges**:
- Time consuming
- Equipment failures
- Weather dependent
- Safety risks
- Limited trials

### Best Practice: Hybrid Approach

1. **Develop in simulation**: Fast iteration
2. **Validate basics on hardware**: Reality check
3. **Refine simulation**: Improve models
4. **Test extensively in sim**: Cover edge cases
5. **Final validation on hardware**: Prove it works

## Reproducibility

### Code

- **Version control**: Git for everything
- **Dependencies**: Document versions (requirements.txt)
- **Seeds**: Set random seeds
- **Documentation**: READMEs and comments
- **Scripts**: Automate experiments

### Data

- **Raw data**: Preserve originals
- **Processing**: Document transformations
- **Metadata**: Collection details
- **Access**: Share publicly when possible

### Hardware

- **Specifications**: Exact models and versions
- **Calibration**: Document procedures and results
- **Configuration**: Save all settings
- **Photos**: Visual documentation

### Procedure

- **Detailed protocol**: Step-by-step instructions
- **Parameters**: All values specified
- **Deviations**: Note any changes
- **Failures**: Document what didn't work

## Research Ethics

### Responsible Research

- **Honesty**: Report accurately
- **Integrity**: Don't fabricate or falsify
- **Objectivity**: Minimize bias
- **Transparency**: Share methods and data
- **Attribution**: Cite others' work properly

### Questionable Practices to Avoid

- Selective reporting of results
- Post-hoc hypothesis generation (HARKing)
- P-hacking and data dredging
- Ignoring negative results
- Insufficient documentation

### Authorship

Who should be an author?
- Significant intellectual contribution
- Involved in drafting or revising
- Approved final version
- Accountable for accuracy

Order typically reflects contribution level.

### IRB and Safety

- Human subjects research requires IRB approval
- Safety review for outdoor flights
- Risk assessment documentation
- Informed consent (if applicable)

## Documentation

### Lab Notebook

**What to record**:
- Date and time
- Objective of session
- Procedures followed
- Observations and results
- Problems encountered
- Ideas for next steps
- Data file references

**Best practices**:
- Write as you go
- Be detailed enough to reproduce
- Include sketches and photos
- Date and sign each entry
- Never erase (cross out instead)

### Code Documentation

**Comments should explain**:
- Why (not what - code shows that)
- Assumptions and limitations
- Parameter meanings
- References to papers/algorithms

**README should include**:
- Purpose and description
- Installation instructions
- Usage examples
- Dependencies
- License

### Experimental Protocol

Write detailed protocol including:
- Equipment setup procedure
- Calibration steps
- Environmental conditions
- Execution steps
- Data collection specifics
- Safety procedures

## Common Pitfalls in Robotics Research

### Problem: "It works in simulation"
**Solution**: Early and frequent hardware testing

### Problem: "It worked yesterday"
**Solution**: Version control, systematic testing

### Problem: "The results are noisy"
**Solution**: More trials, better controls, statistics

### Problem: "We can't reproduce it"
**Solution**: Document everything, save raw data

### Problem: "It only works in our lab"
**Solution**: Test varied conditions, generalization

### Problem: "The battery died"
**Solution**: Power budget, battery swaps, planning

### Problem: "We ran out of time"
**Solution**: Realistic planning, prioritization, MVPs

## Research Tools

### Programming
- Python (primary for prototyping)
- C++ (when performance matters)
- MATLAB (for some algorithms)
- ROS (robot operating system)

### Simulation
- Gazebo (general robotics)
- AirSim (drone-specific)
- PyBullet (physics)
- Unity/Unreal (realistic graphics)

### Data Analysis
- Jupyter notebooks (interactive)
- Pandas (data manipulation)
- NumPy/SciPy (numerical computing)
- Matplotlib/Seaborn (visualization)
- R (advanced statistics)

### Machine Learning
- TensorFlow/Keras
- PyTorch
- scikit-learn
- OpenCV

### Writing
- LaTeX (papers)
- Overleaf (collaborative LaTeX)
- Zotero/Mendeley (references)
- Git (version control for papers)

## Timeline Planning

### Typical PhD Timeline (scaled for undergrad)

**Months 1-2**: Literature review, setup
**Months 3-4**: Initial implementation
**Months 5-6**: Iterative development and testing
**Months 7-8**: Comprehensive experiments
**Months 9-10**: Analysis and refinement
**Months 11-12**: Writing and presentation

### Milestones

Set concrete milestones:
- Literature review complete
- Simulation environment ready
- Baseline method implemented
- Hardware tested
- Experiments 50% complete
- First draft written

### Contingency

Build in slack time:
- Equipment failures
- Unexpected results requiring investigation
- Learning curve for new tools
- Weather delays (outdoor experiments)
- Writer's block

## Next Steps

1. Review [undergraduate research guide](./undergraduate-research-guide.md)
2. Choose research topic from [project ideas](./thesis-project-ideas.md)
3. Draft research proposal
4. Develop detailed experimental protocol
5. Begin with pilot experiments

---

**Good research takes time, rigor, and persistence. Follow these methodologies and your work will be reproducible, credible, and impactful!**
