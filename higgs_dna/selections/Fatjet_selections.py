import numpy as np
import awkward
from higgs_dna.selections.object_selections import delta_r_mask
import math

# def Fatjet_preselection_chatgpt(Fatjet, leading_photon):
#     """
#     Selects the closest Fatjet to the leading photon for each event
#     if the distance is less than 0.8.

#     Parameters:
#     Fatjet (dict): A dictionary with fields 'pt', 'eta', 'phi', 'mass', each being an awkward array.
#     leading_photon (dict): A dictionary with fields 'pt', 'eta', 'phi', 'mass', each being a 1D array.

#     Returns:
#     dict: Filtered Fatjet fields containing only the closest Fatjet within distance < 0.8 per event.
#     """

#     # Calculate the distance between each Fatjet and the leading photon
#     d_eta = Fatjet['eta'] - awkward.Array(leading_photon['eta'])[:, None]
#     d_phi = Fatjet['phi'] - awkward.Array(leading_photon['phi'])[:, None]

#     # Normalize d_phi to be within [-pi, pi]
#     d_phi = (d_phi + np.pi) % (2 * np.pi) - np.pi

#     distance = np.sqrt(d_eta**2 + d_phi**2)

#     # Mask for distances < 0.8
#     mask = distance < 0.8

#     # Apply mask to distances
#     valid_distances = awkward.where(mask, distance, np.inf)

#     # Find index of the closest Fatjet per event
#     closest_indices = awkward.argmin(valid_distances, axis=1, keepdims=True)

#     # Mask to select only valid events where a Fatjet satisfies the condition
#     event_has_valid_fatjet = awkward.min(valid_distances, axis=1) < np.inf

#     # Select closest Fatjet fields
#     filtered_fatjets = {
#         key: awkward.firsts(awkward.fill_none(array[event_has_valid_fatjet][closest_indices[event_has_valid_fatjet]], []), axis=1)
#         for key, array in Fatjet.fields()
#     }

#     return filtered_fatjets

def delta_phi(a, b):
    return (a - b + math.pi) % (2 * math.pi) - math.pi

def delta_r2(eta1, phi1, eta2, phi2):
    return (eta1 - eta2)**2 + delta_phi(phi1, phi2)**2

def select_min(mval: awkward.Array):
    min_values = awkward.min(mval, axis=1, mask_identity=True)
    print(min_values)
    min_values = awkward.flatten(awkward.fill_none(awkward.pad_none(min_values, 1), 999))
    print(min_values)
    min_cut_mval = awkward.where((mval == min_values), mval, 999)
    return min_cut_mval

def delta_r_select(
    first: awkward.highlevel.Array, second: awkward.highlevel.Array, threshold: float
) -> awkward.highlevel.Array:
    mval = first.metric_table(second)
    # mval_cut_min = select_min(mval)
    dr_cut = awkward.all(mval < threshold, axis=-1)
    # dr_cut = awkward.all(mval_cut_min < threshold, axis=-1)
    return dr_cut

# def Fatjet_preselection(
#         self,
#     fatjets: awkward.highlevel.Array,
#     diphotons: awkward.highlevel.Array,
# ) -> awkward.highlevel.Array:
#     # same as select_jets(), but uses fatjet variables
#     pt_cut = fatjets.pt > self.fatjet_pt_threshold
#     eta_cut = abs(fatjets.eta) < self.fatjet_max_eta
#     dr_dipho_cut = awkward.ones_like(pt_cut) > 0
#     #if self.clean_fatjet_dipho & (awkward.count(diphotons) > 0):
#     #   dr_dipho_cut = delta_r_select(fatjets, diphotons, self.fatjet_dipho_max_dr)

#     if (self.clean_fatjet_pho):
#         lead = awkward.zip(
#             {
#                 "pt": diphotons.pho_lead.pt,
#                 "eta": diphotons.pho_lead.eta,
#                 "phi": diphotons.pho_lead.phi,
#                 "mass": diphotons.pho_lead.mass,
#                 "charge": diphotons.pho_lead.charge,
#             }
#         )
#         lead = awkward.with_name(lead, "PtEtaPhiMCandidate")
#         sublead = awkward.zip(
#             {
#                 "pt": diphotons.pho_sublead.pt,
#                 "eta": diphotons.pho_sublead.eta,
#                 "phi": diphotons.pho_sublead.phi,
#                 "mass": diphotons.pho_sublead.mass,
#                 "charge": diphotons.pho_sublead.charge,
#             }
#         )
#         sublead = awkward.with_name(sublead, "PtEtaPhiMCandidate")
#         dr_pho_lead_cut = delta_r_select(fatjets, lead, self.fatjet_pho_max_dr)
#         # dr_pho_sublead_cut = delta_r_select(fatjets, sublead, self.fatjet_pho_max_dr)
#     else:
#         dr_pho_lead_cut = fatjets.pt > -1
#         # dr_pho_sublead_cut = fatjets.pt > -1
    
#     # if (self.clean_fatjet_ele) & (awkward.count(electrons) > 0):
#     #     dr_electrons_cut = delta_r_mask(fatjets, electrons, self.fatjet_ele_min_dr)
#     # else:
#     #     dr_electrons_cut = fatjets.pt > -1

#     # if (self.clean_fatjet_muo) & (awkward.count(muons) > 0):
#     #     dr_muons_cut = delta_r_mask(fatjets, muons, self.fatjet_muo_min_dr)
#     # else:
#     #     dr_muons_cut = fatjets.pt > -1

#     return (
#         (pt_cut)
#         & (eta_cut)
#         & (dr_dipho_cut)
#         & (dr_pho_lead_cut)
#     )

def Fatjet_preselection(
        self,
    fatjets: awkward.highlevel.Array,
    lead_photon: awkward.highlevel.Array,
) -> awkward.highlevel.Array:
    # same as select_jets(), but uses fatjet variables
    pt_cut = fatjets.pt > self.fatjet_pt_threshold
    eta_cut = abs(fatjets.eta) < self.fatjet_max_eta
    dr_dipho_cut = awkward.ones_like(pt_cut) > 0

    if (self.clean_fatjet_pho):
        lead = awkward.zip(
            {
                "pt": lead_photon.pt,
                "eta": lead_photon.eta,
                "phi": lead_photon.phi,
                "mass": lead_photon.mass,
                "charge": lead_photon.charge,
            }
        )
        lead = awkward.with_name(lead, "PtEtaPhiMCandidate")
        dr_pho_lead_cut = delta_r_select(fatjets, lead, self.fatjet_pho_max_dr)
    else:
        dr_pho_lead_cut = fatjets.pt > -1


    return (
        (pt_cut)
        & (eta_cut)
        & (dr_dipho_cut)
        & (dr_pho_lead_cut)
    )
