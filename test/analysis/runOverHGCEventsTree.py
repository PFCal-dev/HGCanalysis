#!/usr/bin/env python

import ROOT
from ROOT import *
from UserCode.HGCanalysis.PlotUtils import *

customROOTstyle()

inF=TFile.Open('HGCSimHitsAnalysis.root')
Events=inF.Get('hgcSimHitsAnalyzer/HGC')

E_eh=3.6*1e-9 #GeV

showerFunc=TF1("showerfunc","[0]*pow(x,[1])*exp(-[2]*x)",0,25);
showerFunc.SetParLimits(1,0.,100.);
showerFunc.SetParLimits(2,0.,100.);
showerFunc.SetLineColor(kBlue);

enVsOverburden = TH2F("envsoverburden",";Distance transversed [1/X_{0}]; Energy [MeV]; Events",50,0,25,100,0,500);
enVsOverburden.Sumw2();
enVsOverburden.SetDirectory(0);

for i in xrange(0,Events.GetEntriesFast()):
    Events.GetEntry(i)
    totalEnPerLayer=30*[0]
    for he in xrange(0,Events.nee):
        print Events.ee_layer[he],Events.ee_module[he]
        layer=Events.ee_layer[he]
        edep=Events.ee_edep[he]*1e3 #/E_eh
        totalEnPerLayer[layer]+=edep

    print '****'

    gr=TGraphErrors()
    gr.SetMarkerStyle(20)
    for val in totalEnPerLayer:
        ip=gr.GetN()
        x=ip*0.5
        if ip>9 : x=(ip-9)*0.8+5
        if ip>19: x=(ip-19)*1.2+13

        gr.SetPoint(ip,x,val)
        gr.SetPointError(ip,0,sqrt(val))

        enVsOverburden.Fill(x,val)

    showerFunc.SetParLimits(0,0.,max(totalEnPerLayer)*1.1);
    gr.Fit(showerFunc,"RQ+")
    
    c=TCanvas('c','c',500,500)
    c.cd()
    gr.Draw('ap')
    gr.GetXaxis().SetTitle('Transversed thickness [1/X_{0}]')
    gr.GetYaxis().SetTitle('Energy deposited [MeV]') #/ E_{eh}')
    gr.GetYaxis().SetTitleOffset(1.2)
    gr.GetXaxis().SetTitleOffset(1.0)
    MyPaveText('CMS/HGCAL simulation')

    chi2=showerFunc.GetChisquare();
    ndof=showerFunc.GetNDF();
    showerMax=showerFunc.GetParameter(1)/showerFunc.GetParameter(2)

    text='[Event %d]\\#chi^{2}/ndof=%3.0f/%d\\max=%3.0f'%(Events.event,chi2,ndof,showerMax)
    MyPaveText(text,0.6,0.6,0.9,0.9).SetTextFont(42)

    c.SaveAs('Event_%d.png'%(Events.event))

inF.Close()

rawProfile=TGraphErrors()
rawProfile.SetMarkerStyle(20)

for xbin in xrange(1,enVsOverburden.GetXaxis().GetNbins()+1):
    htempraw = enVsOverburden.ProjectionY("rawpy",xbin,xbin);
    x        = enVsOverburden.GetXaxis().GetBinCenter(xbin);
    xerr     = enVsOverburden.GetXaxis().GetBinWidth(xbin)/2;
    if htempraw.GetMean()>0 :
        np     = rawProfile.GetN();
        rawProfile.SetPoint(np,x,   htempraw.GetMean())
        rawProfile.SetPointError(np,xerr,htempraw.GetMeanError())

c=TCanvas('c','c',500,500)
c.cd()
rawProfile.Draw('ap')
rawProfile.GetXaxis().SetTitle('Transversed thickness [1/X_{0}]')
rawProfile.GetYaxis().SetTitle('<Energy deposited> [MeV]')
rawProfile.GetYaxis().SetTitleOffset(1.2)
rawProfile.GetXaxis().SetTitleOffset(1.0)
MyPaveText('CMS/HGCAL simulation')
c.SaveAs('cmssw_profile.png')

#
#ce=TCanvas('ce','ce',600,600)
#ce.SetLogy()
#Events.Draw(hitsToPlot+'.myEnergy*1e3')
#he=ce.GetPrimitive('htemp')
#he.GetXaxis().SetTitle('Energy [keV]')
#he.GetYaxis().SetTitle('# hits')
#he.SetFillColor(18)
#heh=PlotHeader()
#ce.SaveAs('HE_E.png')
#
#ct=TCanvas('ct','ct',600,600)
#ct.SetLogy()
#Events.Draw(hitsToPlot+'.myTime')
#ht=ct.GetPrimitive('htemp')
#ht.GetXaxis().SetTitle('Time [ns]')
#ht.GetYaxis().SetTitle('# hits')
#ht.SetFillColor(18)
#hth=PlotHeader()
#ct.SaveAs('HE_T.png')
#
#cte=TCanvas('cte','cte',600,600)
#cte.SetLogz()
#cte.SetRightMargin(0.2)
#Events.Draw(hitsToPlot+'.myTime:hehits.myEnergy*1e3','','colz')
#hte=cte.GetPrimitive('htemp')
#hte.GetXaxis().SetTitle('Time [ns]')
#hte.GetYaxis().SetTitle('Energy [keV]')
#hte.GetYaxis().SetTitleOffset(1.2)
#hte.GetZaxis().SetTitle('# hits')
#hte.GetZaxis().SetTitleOffset(1.5)
#hteh=PlotHeader()
#hteh.Draw()
#cte.SaveAs('HE_EvsT.png')
#
##inF.Close()
#raw_input()
