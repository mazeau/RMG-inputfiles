#!/usr/bin/env python
# encoding: utf-8

name = "Seed_edge"
shortDesc = u""
longDesc = u"""

"""
autoGenerated=True
entry(
    index = 0,
    label = "HCO + X <=> HCO_ads",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(
        A = 0.1,
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Adsorbate;VacantSite]\nEuclidian distance = 0\nfamily: Surface_Adsorption_Single',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Adsorbate;VacantSite]
Euclidian distance = 0
family: Surface_Adsorption_Single
""",
)

entry(
    index = 1,
    label = "glyoxal + X + X <=> HCO_ads + HCO_ads",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(
        A = 0.01,
        n = 0,
        Ea = (41.84, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Adsorbate;VacantSite1;VacantSite2]\nEuclidian distance = 0\nfamily: Surface_Adsorption_Dissociative',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Adsorbate;VacantSite1;VacantSite2]
Euclidian distance = 0
family: Surface_Adsorption_Dissociative
""",
)

entry(
    index = 2,
    label = "[Pt]OC=[Pt] + HCO_ads <=> OCX + [Pt]CO[Pt]",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (5e+17, 'm^2/(mol*s)'),
        n = 0,
        Ea = (40, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Abstracting;R-H]\nEuclidian distance = 0\nfamily: Surface_Abstraction',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Abstracting;R-H]
Euclidian distance = 0
family: Surface_Abstraction
""",
)

entry(
    index = 3,
    label = "[Pt]OC([Pt])C([Pt])O[Pt] <=> [Pt]OC=[Pt] + [Pt]OC=[Pt]",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+09, '1/s'),
        n = 0,
        Ea = (29.288, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Combined]\nEuclidian distance = 0\nfamily: Surface_Bidentate_Dissociation',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Combined]
Euclidian distance = 0
family: Surface_Bidentate_Dissociation
""",
)

entry(
    index = 4,
    label = "OX + [Pt]OC([Pt])C=[Pt] <=> [Pt]OC=[Pt] + [Pt]OC=[Pt]",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+15, 'm^2/(mol*s)'),
        n = 0,
        Ea = (80, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Estimated using template [Abstracting;Donating] for rate rule [Abstracting;R-C]\nEuclidian distance = 1.0\nfamily: Surface_Abstraction',
    ),
    longDesc = 
u"""
Estimated using template [Abstracting;Donating] for rate rule [Abstracting;R-C]
Euclidian distance = 1.0
family: Surface_Abstraction
""",
)

entry(
    index = 5,
    label = "CHX + [Pt]OC([Pt])O[Pt] <=> [Pt]OC=[Pt] + [Pt]OC=[Pt]",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(
        A = (2e+15, 'm^2/(mol*s)'),
        n = 0,
        Ea = (80, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Estimated using template [Abstracting;Donating] for rate rule [Abstracting;R-O]\nEuclidian distance = 1.0\nMultiplied by reaction path degeneracy 2.0\nfamily: Surface_Abstraction',
    ),
    longDesc = 
u"""
Estimated using template [Abstracting;Donating] for rate rule [Abstracting;R-O]
Euclidian distance = 1.0
Multiplied by reaction path degeneracy 2.0
family: Surface_Abstraction
""",
)

entry(
    index = 6,
    label = "[Pt]OC#[Pt] + [Pt]CO[Pt] <=> [Pt]OC=[Pt] + [Pt]OC=[Pt]",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(
        A = (1e+18, 'm^2/(mol*s)'),
        n = 0,
        Ea = (40, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Abstracting;R-H]\nEuclidian distance = 0\nMultiplied by reaction path degeneracy 2.0\nfamily: Surface_Abstraction',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Abstracting;R-H]
Euclidian distance = 0
Multiplied by reaction path degeneracy 2.0
family: Surface_Abstraction
""",
)

entry(
    index = 7,
    label = "[Pt]OC([Pt])O[Pt] <=> OX + [Pt]OC=[Pt]",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(
        A = (2e+09, '1/s'),
        n = 0,
        Ea = (29.288, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Combined]\nEuclidian distance = 0\nMultiplied by reaction path degeneracy 2.0\nfamily: Surface_Bidentate_Dissociation',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Combined]
Euclidian distance = 0
Multiplied by reaction path degeneracy 2.0
family: Surface_Bidentate_Dissociation
""",
)

entry(
    index = 8,
    label = "[Pt]OO[Pt] + CHX <=> OX + [Pt]OC=[Pt]",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(
        A = (2e+15, 'm^2/(mol*s)'),
        n = 0,
        Ea = (80, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Estimated using template [Abstracting;Donating] for rate rule [Abstracting;R-O]\nEuclidian distance = 1.0\nMultiplied by reaction path degeneracy 2.0\nfamily: Surface_Abstraction',
    ),
    longDesc = 
u"""
Estimated using template [Abstracting;Donating] for rate rule [Abstracting;R-O]
Euclidian distance = 1.0
Multiplied by reaction path degeneracy 2.0
family: Surface_Abstraction
""",
)

entry(
    index = 9,
    label = "[Pt]OC#[Pt] + HOX <=> OX + [Pt]OC=[Pt]",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (5e+17, 'm^2/(mol*s)'),
        n = 0,
        Ea = (40, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Abstracting;R-H]\nEuclidian distance = 0\nfamily: Surface_Abstraction',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Abstracting;R-H]
Euclidian distance = 0
family: Surface_Abstraction
""",
)

entry(
    index = 10,
    label = "[Pt]OO[Pt] <=> OX + OX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+09, '1/s'),
        n = 0,
        Ea = (29.288, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Combined]\nEuclidian distance = 0\nfamily: Surface_Bidentate_Dissociation',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Combined]
Euclidian distance = 0
family: Surface_Bidentate_Dissociation
""",
)

entry(
    index = 11,
    label = "OCX + X <=> [Pt]OC#[Pt]",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+14, 'm^2/(mol*s)'),
        n = 0,
        Ea = (589.946, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Combined;VacantSite]\nEuclidian distance = 0\nfamily: Surface_DoubleBond_to_Bidentate',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Combined;VacantSite]
Euclidian distance = 0
family: Surface_DoubleBond_to_Bidentate
""",
)

entry(
    index = 12,
    label = "O=C([Pt])C([Pt])O[Pt] <=> OCX + [Pt]OC=[Pt]",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+09, '1/s'),
        n = 0,
        Ea = (29.288, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Combined]\nEuclidian distance = 0\nfamily: Surface_Bidentate_Dissociation',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Combined]
Euclidian distance = 0
family: Surface_Bidentate_Dissociation
""",
)

entry(
    index = 13,
    label = "O=C([Pt])C=[Pt] + OX <=> OCX + [Pt]OC=[Pt]",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+15, 'm^2/(mol*s)'),
        n = 0,
        Ea = (80, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Estimated using template [Abstracting;Donating] for rate rule [Abstracting;R-C]\nEuclidian distance = 1.0\nfamily: Surface_Abstraction',
    ),
    longDesc = 
u"""
Estimated using template [Abstracting;Donating] for rate rule [Abstracting;R-C]
Euclidian distance = 1.0
family: Surface_Abstraction
""",
)

entry(
    index = 14,
    label = "O=C([Pt])O[Pt] + CHX <=> OCX + [Pt]OC=[Pt]",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+15, 'm^2/(mol*s)'),
        n = 0,
        Ea = (80, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Estimated using template [Abstracting;Donating] for rate rule [Abstracting;R-O]\nEuclidian distance = 1.0\nfamily: Surface_Abstraction',
    ),
    longDesc = 
u"""
Estimated using template [Abstracting;Donating] for rate rule [Abstracting;R-O]
Euclidian distance = 1.0
family: Surface_Abstraction
""",
)

entry(
    index = 15,
    label = "[Pt]OC#[Pt] + HCO_ads <=> OCX + [Pt]OC=[Pt]",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (5e+17, 'm^2/(mol*s)'),
        n = 0,
        Ea = (40, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Abstracting;R-H]\nEuclidian distance = 0\nfamily: Surface_Abstraction',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Abstracting;R-H]
Euclidian distance = 0
family: Surface_Abstraction
""",
)

entry(
    index = 16,
    label = "O=C([Pt])O[Pt] <=> OCX + OX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+09, '1/s'),
        n = 0,
        Ea = (29.288, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Combined]\nEuclidian distance = 0\nfamily: Surface_Bidentate_Dissociation',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Combined]
Euclidian distance = 0
family: Surface_Bidentate_Dissociation
""",
)

entry(
    index = 17,
    label = "OCCOX <=> OCX + OCX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+09, '1/s'),
        n = 0,
        Ea = (29.288, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Combined]\nEuclidian distance = 0\nfamily: Surface_Bidentate_Dissociation',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Combined]
Euclidian distance = 0
family: Surface_Bidentate_Dissociation
""",
)

entry(
    index = 18,
    label = "OH(D) + X <=> HOX",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(
        A = 0.1,
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Adsorbate;VacantSite]\nEuclidian distance = 0\nfamily: Surface_Adsorption_Single',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Adsorbate;VacantSite]
Euclidian distance = 0
family: Surface_Adsorption_Single
""",
)

entry(
    index = 19,
    label = "OX + [Pt]CO[Pt] <=> HOX + [Pt]OC=[Pt]",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(
        A = (1e+18, 'm^2/(mol*s)'),
        n = 0,
        Ea = (40, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Abstracting;R-H]\nEuclidian distance = 0\nMultiplied by reaction path degeneracy 2.0\nfamily: Surface_Abstraction',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Abstracting;R-H]
Euclidian distance = 0
Multiplied by reaction path degeneracy 2.0
family: Surface_Abstraction
""",
)

entry(
    index = 20,
    label = "HOOH + X + X <=> HOX + HOX",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(
        A = 0.01,
        n = 0,
        Ea = (41.84, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Adsorbate;VacantSite1;VacantSite2]\nEuclidian distance = 0\nfamily: Surface_Adsorption_Dissociative',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Adsorbate;VacantSite1;VacantSite2]
Euclidian distance = 0
family: Surface_Adsorption_Dissociative
""",
)

entry(
    index = 21,
    label = "H + X <=> HX",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(
        A = 0.1,
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Adsorbate;VacantSite]\nEuclidian distance = 0\nfamily: Surface_Adsorption_Single',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Adsorbate;VacantSite]
Euclidian distance = 0
family: Surface_Adsorption_Single
""",
)

entry(
    index = 22,
    label = "CH2O + X + X <=> HX + HCO_ads",
    degeneracy = 2.0,
    kinetics = StickingCoefficient(
        A = 0.02,
        n = 0,
        Ea = (41.84, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Adsorbate;VacantSite1;VacantSite2]\nEuclidian distance = 0\nMultiplied by reaction path degeneracy 2.0\nfamily: Surface_Adsorption_Dissociative',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Adsorbate;VacantSite1;VacantSite2]
Euclidian distance = 0
Multiplied by reaction path degeneracy 2.0
family: Surface_Adsorption_Dissociative
""",
)

entry(
    index = 23,
    label = "formic_acid + X + X <=> formyloxyX + HX",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(
        A = 0.01,
        n = 0,
        Ea = (78.6154, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Adsorbate;VacantSite1;VacantSite2]\nEuclidian distance = 0\nfamily: Surface_Adsorption_Dissociative',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Adsorbate;VacantSite1;VacantSite2]
Euclidian distance = 0
family: Surface_Adsorption_Dissociative
""",
)

entry(
    index = 24,
    label = "formic_acid + X + X <=> HOCOX + HX",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(
        A = 0.01,
        n = 0,
        Ea = (41.84, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Adsorbate;VacantSite1;VacantSite2]\nEuclidian distance = 0\nfamily: Surface_Adsorption_Dissociative',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Adsorbate;VacantSite1;VacantSite2]
Euclidian distance = 0
family: Surface_Adsorption_Dissociative
""",
)

entry(
    index = 25,
    label = "CH3 + X <=> CH3X",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(
        A = 0.1,
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Adsorbate;VacantSite]\nEuclidian distance = 0\nfamily: Surface_Adsorption_Single',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Adsorbate;VacantSite]
Euclidian distance = 0
family: Surface_Adsorption_Single
""",
)

entry(
    index = 26,
    label = "CH3CHO + X + X <=> CH3X + HCO_ads",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(
        A = 0.01,
        n = 0,
        Ea = (41.84, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Adsorbate;VacantSite1;VacantSite2]\nEuclidian distance = 0\nfamily: Surface_Adsorption_Dissociative',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Adsorbate;VacantSite1;VacantSite2]
Euclidian distance = 0
family: Surface_Adsorption_Dissociative
""",
)

entry(
    index = 27,
    label = "CH2X + [Pt]CO[Pt] <=> CH3X + [Pt]OC=[Pt]",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(
        A = (1e+18, 'm^2/(mol*s)'),
        n = 0,
        Ea = (40, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Abstracting;R-H]\nEuclidian distance = 0\nMultiplied by reaction path degeneracy 2.0\nfamily: Surface_Abstraction',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Abstracting;R-H]
Euclidian distance = 0
Multiplied by reaction path degeneracy 2.0
family: Surface_Abstraction
""",
)

entry(
    index = 28,
    label = "CH3OH + X + X <=> HOX + CH3X",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(
        A = 0.01,
        n = 0,
        Ea = (41.84, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Adsorbate;VacantSite1;VacantSite2]\nEuclidian distance = 0\nfamily: Surface_Adsorption_Dissociative',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Adsorbate;VacantSite1;VacantSite2]
Euclidian distance = 0
family: Surface_Adsorption_Dissociative
""",
)

entry(
    index = 29,
    label = "C2H6 + X + X <=> CH3X + CH3X",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(
        A = 0.01,
        n = 0,
        Ea = (41.84, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Adsorbate;VacantSite1;VacantSite2]\nEuclidian distance = 0\nfamily: Surface_Adsorption_Dissociative',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Adsorbate;VacantSite1;VacantSite2]
Euclidian distance = 0
family: Surface_Adsorption_Dissociative
""",
)

entry(
    index = 30,
    label = "[Pt]CC([Pt])O[Pt] <=> CH2X + [Pt]OC=[Pt]",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+09, '1/s'),
        n = 0,
        Ea = (29.288, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Combined]\nEuclidian distance = 0\nfamily: Surface_Bidentate_Dissociation',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Combined]
Euclidian distance = 0
family: Surface_Bidentate_Dissociation
""",
)

entry(
    index = 31,
    label = "CH2X + [Pt]OC=[Pt] <=> CHX + [Pt]CO[Pt]",
    degeneracy = 2.0,
    duplicate = True,
    kinetics = SurfaceArrhenius(
        A = (1e+18, 'm^2/(mol*s)'),
        n = 0,
        Ea = (40, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Abstracting;R-H]\nEuclidian distance = 0\nMultiplied by reaction path degeneracy 2.0\nfamily: Surface_Abstraction',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Abstracting;R-H]
Euclidian distance = 0
Multiplied by reaction path degeneracy 2.0
family: Surface_Abstraction
""",
)

entry(
    index = 32,
    label = "[Pt]CC=[Pt] + OX <=> CH2X + [Pt]OC=[Pt]",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+15, 'm^2/(mol*s)'),
        n = 0,
        Ea = (80, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Estimated using template [Abstracting;Donating] for rate rule [Abstracting;R-C]\nEuclidian distance = 1.0\nfamily: Surface_Abstraction',
    ),
    longDesc = 
u"""
Estimated using template [Abstracting;Donating] for rate rule [Abstracting;R-C]
Euclidian distance = 1.0
family: Surface_Abstraction
""",
)

entry(
    index = 33,
    label = "CH2X + [Pt]OC=[Pt] <=> CHX + [Pt]CO[Pt]",
    degeneracy = 1.0,
    duplicate = True,
    kinetics = SurfaceArrhenius(
        A = (1e+15, 'm^2/(mol*s)'),
        n = 0,
        Ea = (80, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Estimated using template [Abstracting;Donating] for rate rule [Abstracting;R-O]\nEuclidian distance = 1.0\nfamily: Surface_Abstraction',
    ),
    longDesc = 
u"""
Estimated using template [Abstracting;Donating] for rate rule [Abstracting;R-O]
Euclidian distance = 1.0
family: Surface_Abstraction
""",
)

entry(
    index = 34,
    label = "[Pt]OC#[Pt] + CH3X <=> CH2X + [Pt]OC=[Pt]",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(
        A = (1.5e+18, 'm^2/(mol*s)'),
        n = 0,
        Ea = (40, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Abstracting;R-H]\nEuclidian distance = 0\nMultiplied by reaction path degeneracy 3.0\nfamily: Surface_Abstraction',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Abstracting;R-H]
Euclidian distance = 0
Multiplied by reaction path degeneracy 3.0
family: Surface_Abstraction
""",
)

entry(
    index = 35,
    label = "[Pt]CO[Pt] <=> CH2X + OX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+09, '1/s'),
        n = 0,
        Ea = (30.9038, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Combined]\nEuclidian distance = 0\nfamily: Surface_Bidentate_Dissociation',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Combined]
Euclidian distance = 0
family: Surface_Bidentate_Dissociation
""",
)

entry(
    index = 36,
    label = "O=C([Pt])C[Pt] <=> OCX + CH2X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+09, '1/s'),
        n = 0,
        Ea = (29.288, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Combined]\nEuclidian distance = 0\nfamily: Surface_Bidentate_Dissociation',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Combined]
Euclidian distance = 0
family: Surface_Bidentate_Dissociation
""",
)

entry(
    index = 37,
    label = "[Pt]CC[Pt] <=> CH2X + CH2X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+09, '1/s'),
        n = 0,
        Ea = (63.1725, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Combined]\nEuclidian distance = 0\nfamily: Surface_Bidentate_Dissociation',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Combined]
Euclidian distance = 0
family: Surface_Bidentate_Dissociation
""",
)

entry(
    index = 38,
    label = "[Pt]OC([Pt])C=[Pt] <=> CHX + [Pt]OC=[Pt]",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+09, '1/s'),
        n = 0,
        Ea = (29.288, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Combined]\nEuclidian distance = 0\nfamily: Surface_Bidentate_Dissociation',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Combined]
Euclidian distance = 0
family: Surface_Bidentate_Dissociation
""",
)

entry(
    index = 39,
    label = "CX + [Pt]CO[Pt] <=> CHX + [Pt]OC=[Pt]",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(
        A = (1e+18, 'm^2/(mol*s)'),
        n = 0,
        Ea = (40, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Abstracting;R-H]\nEuclidian distance = 0\nMultiplied by reaction path degeneracy 2.0\nfamily: Surface_Abstraction',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Abstracting;R-H]
Euclidian distance = 0
Multiplied by reaction path degeneracy 2.0
family: Surface_Abstraction
""",
)

entry(
    index = 40,
    label = "[Pt]=CC=[Pt] + OX <=> CHX + [Pt]OC=[Pt]",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(
        A = (2e+15, 'm^2/(mol*s)'),
        n = 0,
        Ea = (80, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Estimated using template [Abstracting;Donating] for rate rule [Abstracting;R-C]\nEuclidian distance = 1.0\nMultiplied by reaction path degeneracy 2.0\nfamily: Surface_Abstraction',
    ),
    longDesc = 
u"""
Estimated using template [Abstracting;Donating] for rate rule [Abstracting;R-C]
Euclidian distance = 1.0
Multiplied by reaction path degeneracy 2.0
family: Surface_Abstraction
""",
)

entry(
    index = 41,
    label = "[Pt]OC#[Pt] + CH2X <=> CHX + [Pt]OC=[Pt]",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(
        A = (1e+18, 'm^2/(mol*s)'),
        n = 0,
        Ea = (40, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Abstracting;R-H]\nEuclidian distance = 0\nMultiplied by reaction path degeneracy 2.0\nfamily: Surface_Abstraction',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Abstracting;R-H]
Euclidian distance = 0
Multiplied by reaction path degeneracy 2.0
family: Surface_Abstraction
""",
)

entry(
    index = 42,
    label = "O=C([Pt])C=[Pt] <=> OCX + CHX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+09, '1/s'),
        n = 0,
        Ea = (29.288, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Combined]\nEuclidian distance = 0\nfamily: Surface_Bidentate_Dissociation',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Combined]
Euclidian distance = 0
family: Surface_Bidentate_Dissociation
""",
)

entry(
    index = 43,
    label = "[Pt]CC=[Pt] <=> CH2X + CHX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+09, '1/s'),
        n = 0,
        Ea = (29.288, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Combined]\nEuclidian distance = 0\nfamily: Surface_Bidentate_Dissociation',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Combined]
Euclidian distance = 0
family: Surface_Bidentate_Dissociation
""",
)

entry(
    index = 44,
    label = "[Pt]=CC=[Pt] <=> CHX + CHX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+09, '1/s'),
        n = 0,
        Ea = (29.288, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Combined]\nEuclidian distance = 0\nfamily: Surface_Bidentate_Dissociation',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Combined]
Euclidian distance = 0
family: Surface_Bidentate_Dissociation
""",
)

entry(
    index = 45,
    label = "[Pt]OC([Pt])C#[Pt] <=> CX + [Pt]OC=[Pt]",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+09, '1/s'),
        n = 0,
        Ea = (29.288, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Combined]\nEuclidian distance = 0\nfamily: Surface_Bidentate_Dissociation',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Combined]
Euclidian distance = 0
family: Surface_Bidentate_Dissociation
""",
)

entry(
    index = 46,
    label = "[Pt]=CC#[Pt] + OX <=> CX + [Pt]OC=[Pt]",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+15, 'm^2/(mol*s)'),
        n = 0,
        Ea = (80, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Estimated using template [Abstracting;Donating] for rate rule [Abstracting;R-C]\nEuclidian distance = 1.0\nfamily: Surface_Abstraction',
    ),
    longDesc = 
u"""
Estimated using template [Abstracting;Donating] for rate rule [Abstracting;R-C]
Euclidian distance = 1.0
family: Surface_Abstraction
""",
)

entry(
    index = 47,
    label = "[Pt]OC#[Pt] + CHX <=> CX + [Pt]OC=[Pt]",
    degeneracy = 1.0,
    duplicate = True,
    kinetics = SurfaceArrhenius(
        A = (5e+17, 'm^2/(mol*s)'),
        n = 0,
        Ea = (40, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Abstracting;R-H]\nEuclidian distance = 0\nfamily: Surface_Abstraction',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Abstracting;R-H]
Euclidian distance = 0
family: Surface_Abstraction
""",
)

entry(
    index = 48,
    label = "CX + [Pt]OC=[Pt] <=> [Pt]OC#[Pt] + CHX",
    degeneracy = 1.0,
    duplicate = True,
    kinetics = SurfaceArrhenius(
        A = (5e+17, 'm^2/(mol*s)'),
        n = 0,
        Ea = (426.039, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Abstracting;R-H]\nEuclidian distance = 0\nfamily: Surface_Abstraction',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Abstracting;R-H]
Euclidian distance = 0
family: Surface_Abstraction
""",
)

entry(
    index = 49,
    label = "[Pt]OC#[Pt] <=> OX + CX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+09, '1/s'),
        n = 0,
        Ea = (29.288, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Combined]\nEuclidian distance = 0\nfamily: Surface_Bidentate_Dissociation',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Combined]
Euclidian distance = 0
family: Surface_Bidentate_Dissociation
""",
)

entry(
    index = 50,
    label = "O=C([Pt])C#[Pt] <=> OCX + CX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+09, '1/s'),
        n = 0,
        Ea = (29.288, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Combined]\nEuclidian distance = 0\nfamily: Surface_Bidentate_Dissociation',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Combined]
Euclidian distance = 0
family: Surface_Bidentate_Dissociation
""",
)

entry(
    index = 51,
    label = "[Pt]CC#[Pt] <=> CH2X + CX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+09, '1/s'),
        n = 0,
        Ea = (29.288, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Combined]\nEuclidian distance = 0\nfamily: Surface_Bidentate_Dissociation',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Combined]
Euclidian distance = 0
family: Surface_Bidentate_Dissociation
""",
)

entry(
    index = 52,
    label = "[Pt]=CC#[Pt] <=> CHX + CX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+09, '1/s'),
        n = 0,
        Ea = (29.288, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Combined]\nEuclidian distance = 0\nfamily: Surface_Bidentate_Dissociation',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Combined]
Euclidian distance = 0
family: Surface_Bidentate_Dissociation
""",
)

entry(
    index = 53,
    label = "[Pt]#CC#[Pt] <=> CX + CX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+09, '1/s'),
        n = 0,
        Ea = (29.288, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Combined]\nEuclidian distance = 0\nfamily: Surface_Bidentate_Dissociation',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Combined]
Euclidian distance = 0
family: Surface_Bidentate_Dissociation
""",
)

